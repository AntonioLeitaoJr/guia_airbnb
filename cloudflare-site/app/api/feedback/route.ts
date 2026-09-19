import { getDb } from "../../../db";
import { guestFeedback } from "../../../db/schema";

type FeedbackPayload = {
  language?: string;
  enjoyedStay?: string;
  wouldRecommend?: string;
  bookingChannel?: string;
  highlight?: string;
  improvement?: string;
  guestName?: string;
  finalMessage?: string;
};

const clean = (value: unknown, max: number) =>
  typeof value === "string" ? value.trim().slice(0, max) : "";

export async function POST(request: Request) {
  try {
    const payload = (await request.json()) as FeedbackPayload;
    const values = {
      language: clean(payload.language, 2) || "pt",
      enjoyedStay: clean(payload.enjoyedStay, 8),
      wouldRecommend: clean(payload.wouldRecommend, 8),
      bookingChannel: clean(payload.bookingChannel, 40),
      highlight: clean(payload.highlight, 800),
      improvement: clean(payload.improvement, 800),
      guestName: clean(payload.guestName, 120),
      finalMessage: clean(payload.finalMessage, 1200),
    };

    if (!values.guestName || !values.enjoyedStay || !values.wouldRecommend || !values.bookingChannel) {
      return Response.json({ error: "required_fields" }, { status: 400 });
    }

    await getDb().insert(guestFeedback).values(values);
    return Response.json({ ok: true }, { status: 201 });
  } catch (error) {
    console.error("feedback_submission_failed", error);
    return Response.json({ error: "temporarily_unavailable" }, { status: 503 });
  }
}
