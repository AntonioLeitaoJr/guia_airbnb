CREATE TABLE `guest_feedback` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`language` text DEFAULT 'pt' NOT NULL,
	`enjoyed_stay` text NOT NULL,
	`would_recommend` text NOT NULL,
	`booking_channel` text NOT NULL,
	`highlight` text DEFAULT '' NOT NULL,
	`improvement` text DEFAULT '' NOT NULL,
	`guest_name` text NOT NULL,
	`final_message` text DEFAULT '' NOT NULL,
	`created_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL
);
