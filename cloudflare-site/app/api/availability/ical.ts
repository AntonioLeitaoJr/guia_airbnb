export type BlockedPeriod = { start: string; end: string };

// Booking's all-day DTEND is exclusive: checkout day may be used for a new arrival.
export function parseBlockedPeriods(calendar: string): BlockedPeriod[] {
  if (!/BEGIN:VCALENDAR/i.test(calendar) || !/END:VCALENDAR/i.test(calendar)) {
    throw new Error("invalid_calendar");
  }

  const lines = calendar.replace(/\r\n[ \t]|\n[ \t]/g, "").split(/\r?\n/);
  const periods: BlockedPeriod[] = [];
  let event: Record<string, string> | null = null;

  for (const line of lines) {
    if (line === "BEGIN:VEVENT") { event = {}; continue; }
    if (line === "END:VEVENT") {
      if (event && event.STATUS !== "CANCELLED" && event.TRANSP !== "TRANSPARENT") {
        const start = calendarDate(event.DTSTART);
        const end = calendarDate(event.DTEND);
        if (start && end && end > start) periods.push({ start, end });
      }
      event = null;
      if (periods.length > 2000) throw new Error("calendar_too_large");
      continue;
    }
    if (!event) continue;
    const colon = line.indexOf(":");
    if (colon < 0) continue;
    const name = line.slice(0, colon).split(";")[0].toUpperCase();
    if (["DTSTART", "DTEND", "STATUS", "TRANSP"].includes(name)) event[name] = line.slice(colon + 1).trim();
  }

  return periods.sort((a, b) => a.start.localeCompare(b.start));
}

function calendarDate(value?: string): string | null {
  const match = /^(\d{4})(\d{2})(\d{2})(?:T\d{6}Z?)?$/.exec(value ?? "");
  if (!match) return null;
  const [, year, month, day] = match;
  const date = `${year}-${month}-${day}`;
  const parsed = new Date(`${date}T00:00:00.000Z`);
  return !Number.isNaN(parsed.getTime()) && parsed.toISOString().startsWith(date) ? date : null;
}
