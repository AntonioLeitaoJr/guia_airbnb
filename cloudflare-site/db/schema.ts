import { sql } from "drizzle-orm";
import { integer, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const guestFeedback = sqliteTable("guest_feedback", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  language: text("language").notNull().default("pt"),
  enjoyedStay: text("enjoyed_stay").notNull(),
  wouldRecommend: text("would_recommend").notNull(),
  bookingChannel: text("booking_channel").notNull(),
  highlight: text("highlight").notNull().default(""),
  improvement: text("improvement").notNull().default(""),
  guestName: text("guest_name").notNull(),
  finalMessage: text("final_message").notNull().default(""),
  createdAt: text("created_at").notNull().default(sql`CURRENT_TIMESTAMP`),
});
