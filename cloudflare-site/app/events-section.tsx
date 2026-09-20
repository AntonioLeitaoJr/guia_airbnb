"use client";

import { useEffect, useMemo, useState } from "react";
import { ArrowUpRight, CalendarDays, Clock3, MapPin, RefreshCw, Sparkles } from "lucide-react";

type Language = "pt" | "en" | "es";
type CityEvent = {
  id: string;
  name: string;
  date: string;
  endDate?: string;
  venue: string;
  url?: string;
  kind: "live" | "annual";
  source: string;
};

const content = {
  pt: {
    eyebrow: "Belém em movimento",
    title: "Eventos para viver a cidade.",
    intro: "Uma agenda que combina atrações com data marcada e tradições que voltam todos os anos.",
    upcoming: "Próximos eventos",
    annual: "Eventos anuais",
    all: "Tudo",
    loading: "Atualizando a agenda de Belém...",
    empty: "Nenhum evento encontrado neste filtro.",
    source: "Fonte",
    details: "Ver detalhes",
    updated: "Agenda atualizada",
  },
  en: {
    eyebrow: "Belém in motion",
    title: "Events to experience the city.",
    intro: "A calendar combining scheduled attractions with traditions that return every year.",
    upcoming: "Upcoming events",
    annual: "Annual events",
    all: "All",
    loading: "Updating the Belém calendar...",
    empty: "No events found for this filter.",
    source: "Source",
    details: "View details",
    updated: "Calendar updated",
  },
  es: {
    eyebrow: "Belém en movimiento",
    title: "Eventos para vivir la ciudad.",
    intro: "Una agenda que combina atracciones programadas y tradiciones que regresan cada año.",
    upcoming: "Próximos eventos",
    annual: "Eventos anuales",
    all: "Todo",
    loading: "Actualizando la agenda de Belém...",
    empty: "No se encontraron eventos en este filtro.",
    source: "Fuente",
    details: "Ver detalles",
    updated: "Agenda actualizada",
  },
} as const;

const localeByLanguage = { pt: "pt-BR", en: "en-US", es: "es-ES" } as const;

export function EventsSection({ language }: { language: Language }) {
  const [events, setEvents] = useState<CityEvent[]>([]);
  const [filter, setFilter] = useState<"all" | "live" | "annual">("live");
  const [loading, setLoading] = useState(true);
  const [updatedAt, setUpdatedAt] = useState("");
  const t = content[language];

  useEffect(() => {
    let active = true;
    fetch("/api/events")
      .then((response) => response.ok ? response.json() : Promise.reject())
      .then((data: { events: CityEvent[]; updatedAt: string }) => {
        if (!active) return;
        setEvents(data.events);
        setUpdatedAt(data.updatedAt);
      })
      .catch(() => undefined)
      .finally(() => active && setLoading(false));
    return () => { active = false; };
  }, []);

  const visibleEvents = useMemo(() => events.filter((event) => filter === "all" || event.kind === filter), [events, filter]);
  const formatter = new Intl.DateTimeFormat(localeByLanguage[language], { day: "2-digit", month: "short", year: "numeric", timeZone: "America/Belem" });

  return (
    <section className="events-section" id="eventos">
      <div className="events-inner">
        <div className="events-heading-row">
          <div className="section-heading">
            <span>{t.eyebrow}</span>
            <h2>{t.title}</h2>
            <p>{t.intro}</p>
          </div>
          <div className="event-filters" aria-label="Filtros de eventos">
            {(["all", "live", "annual"] as const).map((value) => (
              <button key={value} onClick={() => setFilter(value)} className={filter === value ? "active" : ""} aria-pressed={filter === value}>
                {value === "all" ? t.all : value === "live" ? t.upcoming : t.annual}
              </button>
            ))}
          </div>
        </div>

        {loading ? <div className="events-state"><RefreshCw className="spin" /> {t.loading}</div> : visibleEvents.length === 0 ? <div className="events-state">{t.empty}</div> : (
          <div className="events-grid">
            {visibleEvents.map((event) => (
              <article className="event-card" key={event.id}>
                <div className="event-date"><CalendarDays /><strong>{formatter.format(new Date(`${event.date}T12:00:00-03:00`))}</strong></div>
                <span className={`event-kind ${event.kind}`}><Sparkles /> {event.kind === "live" ? t.upcoming : t.annual}</span>
                <h3>{event.name}</h3>
                <p><MapPin /> {event.venue}</p>
                <div className="event-footer"><small>{t.source}: {event.source}</small>{event.url && <a href={event.url} target="_blank" rel="noreferrer">{t.details}<ArrowUpRight /></a>}</div>
              </article>
            ))}
          </div>
        )}
        {updatedAt && <p className="events-updated"><Clock3 /> {t.updated}: {formatter.format(new Date(updatedAt))}</p>}
      </div>
    </section>
  );
}
