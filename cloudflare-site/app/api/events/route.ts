type EventItem = {
  id: string;
  name: string;
  date: string;
  endDate?: string;
  venue: string;
  url?: string;
  kind: "live" | "annual";
  source: string;
};

const iso = (date: Date) => date.toISOString().slice(0, 10);

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
  const arraial = future(new Date(Date.UTC(thisYear, 5, 1)), () => new Date(Date.UTC(thisYear + 1, 5, 1)));
  const bookFair = future(new Date(Date.UTC(thisYear, 7, 1)), () => new Date(Date.UTC(thisYear + 1, 7, 1)));

  return [
    { id: `cirio-${cirio.getUTCFullYear()}`, name: "Círio de Nazaré", date: iso(cirio), venue: "Nazaré e centro histórico de Belém", kind: "annual", source: "Calendário tradicional de Belém", url: "https://ciriodenazare.com.br/" },
    { id: `carnaval-${carnival.getUTCFullYear()}`, name: "Carnaval de Belém", date: iso(carnival), venue: "Programação em diferentes pontos da cidade", kind: "annual", source: "Calendário nacional" },
    { id: `arraial-${arraial.getUTCFullYear()}`, name: "Temporada de arraiais", date: iso(arraial), venue: "Belém · datas específicas a confirmar", kind: "annual", source: "Calendário cultural anual" },
    { id: `feira-livro-${bookFair.getUTCFullYear()}`, name: "Feira Pan-Amazônica do Livro e das Multivozes", date: iso(bookFair), venue: "Belém · data e local a confirmar", kind: "annual", source: "Calendário cultural anual" },
  ];
}

async function ticketmasterEvents(): Promise<EventItem[]> {
  const apiKey = process.env.TICKETMASTER_API_KEY;
  if (!apiKey) return [];
  const now = new Date();
  const oneYearFromNow = new Date(now);
  oneYearFromNow.setUTCFullYear(oneYearFromNow.getUTCFullYear() + 1);
  const params = new URLSearchParams({
    apikey: apiKey,
    latlong: "-1.4558,-48.4902",
    radius: "100",
    unit: "km",
    countryCode: "BR",
    startDateTime: now.toISOString().replace(/\.\d{3}Z$/, "Z"),
    endDateTime: oneYearFromNow.toISOString().replace(/\.\d{3}Z$/, "Z"),
    locale: "*",
    size: "20",
    sort: "date,asc",
  });
  const response = await fetch(`https://app.ticketmaster.com/discovery/v2/events.json?${params}`, {
    headers: { accept: "application/json" },
  });
  if (!response.ok) return [];
  const payload = await response.json() as { _embedded?: { events?: Array<Record<string, any>> } };
  return (payload._embedded?.events ?? []).flatMap((event) => {
    const date = event.dates?.start?.localDate;
    if (!date || !event.name || !event.id) return [];
    return [{
      id: `tm-${event.id}`,
      name: String(event.name),
      date: String(date),
      venue: String(event._embedded?.venues?.[0]?.name ?? "Belém"),
      url: typeof event.url === "string" ? event.url : undefined,
      kind: "live" as const,
      source: "Ticketmaster",
    }];
  });
}

export async function GET() {
  const now = new Date();
  let live: EventItem[] = [];
  try {
    live = await ticketmasterEvents();
  } catch (error) {
    console.error("events_source_unavailable", error);
  }
  const events = [...live, ...nextAnnualEvents(now)].sort((a, b) => a.date.localeCompare(b.date));
  return Response.json({ events, updatedAt: now.toISOString() }, { headers: { "cache-control": "public, max-age=3600, s-maxage=21600, stale-while-revalidate=43200" } });
}
