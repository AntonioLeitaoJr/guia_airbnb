type EventItem = {
  id: string;
  name: string;
  date?: string;
  endDate?: string;
  venue: string;
  url?: string;
  kind: "live" | "annual";
  dateStatus: "confirmed" | "calendar" | "unconfirmed";
  source: string;
};

const iso = (date: Date) => date.toISOString().slice(0, 10);
const TICKETMASTER_ENDPOINT = "https://app.ticketmaster.com/discovery/v2/events.json";
const BELEM_GEOPOINT = "6ztx8wf";
const PAGE_SIZE = 100;
const MAX_PAGES_PER_SEARCH = 5;

function secondSundayOfOctober(year: number) {
  const date = new Date(Date.UTC(year, 9, 1));
  const firstSunday = 1 + ((7 - date.getUTCDay()) % 7);
  return new Date(Date.UTC(year, 9, firstSunday + 7));
}

function easterSunday(year: number) {
  const a = year % 19;
  const b = Math.floor(year / 100);
  const c = year % 100;
  const d = Math.floor(b / 4);
  const e = b % 4;
  const f = Math.floor((b + 8) / 25);
  const g = Math.floor((b - f + 1) / 3);
  const h = (19 * a + b - d - g + 15) % 30;
  const i = Math.floor(c / 4);
  const k = c % 4;
  const l = (32 + 2 * e + 2 * i - h - k) % 7;
  const m = Math.floor((a + 11 * h + 22 * l) / 451);
  const month = Math.floor((h + l - 7 * m + 114) / 31);
  const day = ((h + l - 7 * m + 114) % 31) + 1;
  return new Date(Date.UTC(year, month - 1, day));
}

function nextAnnualEvents(now: Date): EventItem[] {
  const thisYear = now.getUTCFullYear();
  const future = (candidate: Date, next: () => Date) => candidate >= now ? candidate : next();
  const cirio = future(secondSundayOfOctober(thisYear), () => secondSundayOfOctober(thisYear + 1));
  const carnivalFor = (year: number) => {
    const date = easterSunday(year);
    date.setUTCDate(date.getUTCDate() - 47);
    return date;
  };
  const carnival = future(carnivalFor(thisYear), () => carnivalFor(thisYear + 1));

  return [
    {
      id: `cirio-${cirio.getUTCFullYear()}`,
      name: "Círio de Nazaré",
      date: iso(cirio),
      venue: "Nazaré e centro histórico de Belém",
      kind: "annual",
      dateStatus: "calendar",
      source: "Calendário tradicional de Belém",
      url: "https://ciriodenazare.com.br/",
    },
    {
      id: `carnaval-${carnival.getUTCFullYear()}`,
      name: "Carnaval de Belém",
      date: iso(carnival),
      venue: "Programação em diferentes pontos da cidade",
      kind: "annual",
      dateStatus: "calendar",
      source: "Calendário nacional",
    },
    {
      id: "arraial-next",
      name: "Temporada de arraiais",
      venue: "Belém · programação da próxima temporada a confirmar",
      kind: "annual",
      dateStatus: "unconfirmed",
      source: "Calendário cultural anual",
    },
    {
      id: "feira-livro-next",
      name: "Feira Pan-Amazônica do Livro e das Multivozes",
      venue: "Belém · próxima edição com data e local a confirmar",
      kind: "annual",
      dateStatus: "unconfirmed",
      source: "Calendário cultural anual",
    },
  ];
}

type TicketmasterVenue = {
  name?: string;
};

type TicketmasterEvent = {
  id?: string;
  name?: string;
  url?: string;
  dates?: { start?: { localDate?: string } };
  _embedded?: { venues?: TicketmasterVenue[] };
};

type TicketmasterPayload = {
  _embedded?: { events?: TicketmasterEvent[] };
  page?: { number?: number; totalPages?: number; totalElements?: number };
};

type TicketmasterResult = {
  events: EventItem[];
  status: "ok" | "missing_key" | "unauthorized" | "empty" | "unavailable";
  diagnostics?: {
    searches: number;
    pages: number;
    rawEvents: number;
    uniqueEvents: number;
  };
};

function normalizeTicketmasterEvent(event: TicketmasterEvent): EventItem | null {
  const date = event.dates?.start?.localDate;
  if (!date || !event.name || !event.id) return null;
  return {
    id: `tm-${event.id}`,
    name: String(event.name),
    date: String(date),
    venue: String(event._embedded?.venues?.[0]?.name ?? "Belém"),
    url: typeof event.url === "string" ? event.url : undefined,
    kind: "live",
    dateStatus: "confirmed",
    source: "Ticketmaster",
  };
}

async function fetchTicketmasterSearch(baseParams: Record<string, string>) {
  const events: EventItem[] = [];
  let pages = 0;
  let rawEvents = 0;

  for (let page = 0; page < MAX_PAGES_PER_SEARCH; page += 1) {
    const params = new URLSearchParams({ ...baseParams, page: String(page) });
    const response = await fetch(`${TICKETMASTER_ENDPOINT}?${params}`, {
      headers: { accept: "application/json" },
    });

    if (response.status === 401 || response.status === 403) {
      return { events: [], pages, rawEvents, unauthorized: true, successful: false };
    }
    if (!response.ok) {
      return { events, pages, rawEvents, unauthorized: false, successful: pages > 0 };
    }

    pages += 1;
    const payload = await response.json() as TicketmasterPayload;
    const pageEvents = payload._embedded?.events ?? [];
    rawEvents += pageEvents.length;
    for (const rawEvent of pageEvents) {
      const event = normalizeTicketmasterEvent(rawEvent);
      if (event) events.push(event);
    }

    const totalPages = payload.page?.totalPages ?? 0;
    if (pageEvents.length === 0 || page + 1 >= totalPages) break;

    // Ticketmaster's default quota is 5 requests/second. Keep sequential
    // pagination below that threshold when more than one page is necessary.
    await new Promise((resolve) => setTimeout(resolve, 225));
  }

  return { events, pages, rawEvents, unauthorized: false, successful: true };
}

async function ticketmasterEvents(): Promise<TicketmasterResult> {
  const apiKey = process.env.TICKETMASTER_API_KEY;
  if (!apiKey) return { events: [], status: "missing_key" };

  const now = new Date();
  const oneYearFromNow = new Date(now);
  oneYearFromNow.setUTCFullYear(oneYearFromNow.getUTCFullYear() + 1);
  const commonParams = {
    apikey: apiKey,
    countryCode: "BR",
    startDateTime: now.toISOString().replace(/\.\d{3}Z$/, "Z"),
    endDateTime: oneYearFromNow.toISOString().replace(/\.\d{3}Z$/, "Z"),
    locale: "*",
    includeTBA: "no",
    includeTBD: "no",
    size: String(PAGE_SIZE),
    sort: "date,asc",
  };

  // Run both strategies and merge them. The geographic search catches nearby
  // venues while the city search catches records whose venue metadata is tied
  // explicitly to Belém. geoPoint replaces Ticketmaster's deprecated latlong.
  const searches: Array<Record<string, string>> = [
    { ...commonParams, geoPoint: BELEM_GEOPOINT, radius: "150", unit: "km" },
    { ...commonParams, city: "Belém" },
  ];

  const merged = new Map<string, EventItem>();
  let sawSuccessfulResponse = false;
  let pages = 0;
  let rawEvents = 0;

  for (const search of searches) {
    const result = await fetchTicketmasterSearch(search);
    if (result.unauthorized) return { events: [], status: "unauthorized" };
    sawSuccessfulResponse ||= result.successful;
    pages += result.pages;
    rawEvents += result.rawEvents;
    for (const event of result.events) merged.set(event.id, event);
  }

  const events = [...merged.values()].sort((a, b) => (a.date ?? "9999-12-31").localeCompare(b.date ?? "9999-12-31"));
  return {
    events,
    status: events.length > 0 ? "ok" : sawSuccessfulResponse ? "empty" : "unavailable",
    diagnostics: {
      searches: searches.length,
      pages,
      rawEvents,
      uniqueEvents: events.length,
    },
  };
}

export async function GET() {
  const now = new Date();
  let ticketmaster: TicketmasterResult = { events: [], status: "unavailable" };
  try {
    ticketmaster = await ticketmasterEvents();
  } catch (error) {
    console.error("events_source_unavailable", error);
  }

  const events = [...ticketmaster.events, ...nextAnnualEvents(now)].sort((a, b) => {
    if (a.date && b.date) return a.date.localeCompare(b.date);
    if (a.date) return -1;
    if (b.date) return 1;
    return a.name.localeCompare(b.name, "pt-BR");
  });

  return Response.json(
    {
      events,
      updatedAt: now.toISOString(),
      sources: {
        ticketmaster: ticketmaster.status,
        ticketmasterDiagnostics: ticketmaster.diagnostics,
      },
    },
    {
      headers: {
        "cache-control": "public, max-age=300, s-maxage=21600, stale-while-revalidate=86400",
      },
    },
  );
}
