"use client";

import { useEffect, useMemo, useState } from "react";
import { ArrowUpRight, ChevronLeft, ChevronRight } from "lucide-react";

type Language = "pt" | "en" | "es";
type Period = { start: string; end: string };
type AvailabilityResponse = { status: string; periods: Period[]; checkedAt: string };
const bookingUrl = "https://www.booking.com/hotel/br/apartamento-no-coracao-da-amazonia.pt-br.html";
const locales = { pt: "pt-BR", en: "en-US", es: "es-ES" } as const;
const copy = {
  pt: { eyebrow: "Planeje sua estadia", title: "Veja as datas bloqueadas.", intro: "Calendário de reservas e bloqueios exportado da Booking.com. As demais datas precisam de confirmação.", blocked: "Indisponível", consult: "Consulte disponibilidade", pending: "Consultando o calendário...", unavailable: "Calendário temporariamente indisponível. Consulte as datas diretamente na Booking.com.", checked: "Última consulta", disclaimer: "A sincronização não é instantânea. Confirme preço e disponibilidade antes de reservar.", booking: "Conferir na Booking.com", previous: "Mês anterior", next: "Próximo mês" },
  en: { eyebrow: "Plan your stay", title: "See blocked dates.", intro: "Bookings and blocked dates exported from Booking.com. All other dates require confirmation.", blocked: "Unavailable", consult: "Check availability", pending: "Checking the calendar...", unavailable: "Calendar temporarily unavailable. Check dates directly on Booking.com.", checked: "Last checked", disclaimer: "Sync is not instant. Confirm price and availability before booking.", booking: "Check on Booking.com", previous: "Previous month", next: "Next month" },
  es: { eyebrow: "Planifica tu estancia", title: "Consulta las fechas bloqueadas.", intro: "Reservas y bloqueos exportados de Booking.com. Las demás fechas requieren confirmación.", blocked: "No disponible", consult: "Consultar disponibilidad", pending: "Consultando el calendario...", unavailable: "Calendario temporalmente no disponible. Consulta las fechas en Booking.com.", checked: "Última consulta", disclaimer: "La sincronización no es instantánea. Confirma precio y disponibilidad antes de reservar.", booking: "Consultar en Booking.com", previous: "Mes anterior", next: "Mes siguiente" },
} as const;

function todayInBelem() {
  const parts = new Intl.DateTimeFormat("en-US", { year: "numeric", month: "2-digit", day: "2-digit", timeZone: "America/Belem" }).formatToParts(new Date());
  const value = (type: string) => parts.find((part) => part.type === type)?.value ?? "";
  return `${value("year")}-${value("month")}-${value("day")}`;
}

export function AvailabilityCalendar({ language }: { language: Language }) {
  const [today] = useState(todayInBelem);
  const [offset, setOffset] = useState(0);
  const [periods, setPeriods] = useState<Period[]>([]);
  const [checkedAt, setCheckedAt] = useState("");
  const [state, setState] = useState<"loading" | "ok" | "unavailable">("loading");
  const t = copy[language];

  useEffect(() => {
    const controller = new AbortController();
    fetch("/api/availability", { signal: controller.signal })
      .then((response): Promise<AvailabilityResponse> => response.ok ? response.json() : Promise.reject())
      .then((data) => {
        if (data.status !== "ok" || !Array.isArray(data.periods)) throw new Error("invalid_response");
        setPeriods(data.periods);
        setCheckedAt(data.checkedAt);
        setState("ok");
      })
      .catch(() => { if (!controller.signal.aborted) setState("unavailable"); });
    return () => controller.abort();
  }, []);

  const first = useMemo(() => {
    const [year, month] = today.split("-").map(Number);
    return new Date(Date.UTC(year, month - 1 + offset, 1));
  }, [today, offset]);
  const year = first.getUTCFullYear();
  const month = first.getUTCMonth();
  const firstWeekday = (first.getUTCDay() + 6) % 7;
  const length = new Date(Date.UTC(year, month + 1, 0)).getUTCDate();
  const title = new Intl.DateTimeFormat(locales[language], { month: "long", year: "numeric", timeZone: "UTC" }).format(first);
  const weekdays = Array.from({ length: 7 }, (_, index) => new Intl.DateTimeFormat(locales[language], { weekday: "short", timeZone: "UTC" }).format(new Date(Date.UTC(2024, 0, 1 + index))));
  const lastChecked = checkedAt ? new Intl.DateTimeFormat(locales[language], { dateStyle: "short", timeStyle: "short", timeZone: "America/Belem" }).format(new Date(checkedAt)) : "";

  return (
    <section className="availability-panel" aria-labelledby="availability-title">
      <div className="availability-copy">
        <span className="review-eyebrow">{t.eyebrow}</span>
        <h3 id="availability-title">{t.title}</h3>
        <p>{t.intro}</p>
        <div className="availability-legend"><span><i className="availability-dot blocked" />{t.blocked}</span><span><i className="availability-dot consult" />{t.consult}</span></div>
        <p className="availability-note">{t.disclaimer}</p>
        <a className="availability-booking" href={bookingUrl} target="_blank" rel="noopener noreferrer">{t.booking}<ArrowUpRight size={18} /></a>
      </div>
      <div className="availability-widget">
        <div className="availability-month"><button type="button" onClick={() => setOffset((value) => Math.max(0, value - 1))} disabled={offset === 0} aria-label={t.previous}><ChevronLeft /></button><strong aria-live="polite">{title}</strong><button type="button" onClick={() => setOffset((value) => Math.min(11, value + 1))} disabled={offset === 11} aria-label={t.next}><ChevronRight /></button></div>
        {state === "ok" ? <>
          <div className="availability-grid" role="grid" aria-label={title}>
            {weekdays.map((day, index) => <span className="availability-weekday" key={index}>{day}</span>)}
            {Array.from({ length: firstWeekday }, (_, index) => <span key={`empty-${index}`} aria-hidden="true" />)}
            {Array.from({ length }, (_, index) => {
              const day = index + 1;
              const date = `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
              const past = date < today;
              const blocked = periods.some((period) => date >= period.start && date < period.end);
              return <span key={date} role="gridcell" aria-label={`${day} ${title}: ${past ? "" : blocked ? t.blocked : t.consult}`} className={`availability-day${past ? " past" : blocked ? " blocked" : " consult"}`}>{day}</span>;
            })}
          </div>
          <small className="availability-status">{t.checked}: {lastChecked}</small>
        </> : <p className="availability-status" role="status">{state === "loading" ? t.pending : t.unavailable}</p>}
      </div>
    </section>
  );
}
