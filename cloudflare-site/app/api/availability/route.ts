import { parseBlockedPeriods } from "./ical";

const unavailable = () => Response.json({ status: "unavailable", periods: [] }, {
  status: 503,
  headers: { "cache-control": "no-store" },
});

export async function GET() {
  const secret = process.env.BOOKING_ICAL_URL;
  if (!secret) return unavailable();

  try {
    const url = new URL(secret);
    if (url.protocol !== "https:" || url.hostname !== "ical.booking.com" || url.pathname !== "/v1/export") {
      return unavailable();
    }
    const response = await fetch(url, { signal: AbortSignal.timeout(8000) });
    if (!response.ok || Number(response.headers.get("content-length")) > 1024 * 1024) return unavailable();
    const body = await response.text();
    if (body.length > 1024 * 1024) return unavailable();
    const periods = parseBlockedPeriods(body);
    return Response.json({ status: "ok", periods, checkedAt: new Date().toISOString() }, {
      headers: { "cache-control": "public, max-age=300, s-maxage=900" },
    });
  } catch (error) {
    console.error("booking_calendar_unavailable", error instanceof Error ? error.name : "unknown");
    return unavailable();
  }
}
