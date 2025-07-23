from telegram.ext import ApplicationBuilder, CommandHandler

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.run_polling()

if __name__ == "__main__":
    main()
