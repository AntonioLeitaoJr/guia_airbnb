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

const sitesFeedbackProxy =
  "https://torre-evidence-guia.artoriusjr.chatgpt.site/api/feedback";

async function sendToSpreadsheet(request: Request, values: FeedbackPayload) {
  const webhookUrl = process.env.GOOGLE_SHEETS_WEBHOOK_URL;
  const requestHost = new URL(request.url).hostname;

  // The public Cloudflare deployment proxies through the Sites deployment,
  // where the Google Apps Script URL is stored as a protected runtime value.
  const destination = webhookUrl
    ? webhookUrl
    : requestHost !== "torre-evidence-guia.artoriusjr.chatgpt.site"
      ? sitesFeedbackProxy
      : "";

  if (!destination) {
    throw new Error("feedback_webhook_not_configured");
  }

  const response = await fetch(destination, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(values),
    redirect: "follow",
    signal: AbortSignal.timeout(12_000),
  });

  if (!response.ok) {
    throw new Error(`feedback_webhook_http_${response.status}`);
  }

  const body = await response.text();
  if (body) {
    try {
      const result = JSON.parse(body) as { ok?: boolean };
      if (result.ok === false) throw new Error("feedback_webhook_rejected");
    } catch (error) {
      if (error instanceof SyntaxError) {
        // Some Apps Script deployments return an empty or non-JSON success body.
      } else {
        throw error;
      }
    }
  }
}

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

    await sendToSpreadsheet(request, values);
    return Response.json({ ok: true }, { status: 201 });
  } catch (error) {
    console.error("feedback_submission_failed", error);
    return Response.json({ error: "temporarily_unavailable" }, { status: 503 });
  }
}
