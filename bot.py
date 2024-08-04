import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Configurer le logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s',
    level=logging.INFO
)

# Remplace TOKEN par le token de ton bot
TOKEN = '7308087673:AAH5-UEVxBpar77uCKGNDbrSLyBjezs7T_s'
IMAGE_URL = 'https://www.snipes.fr/dw/image/v2/BDCB_PRD/on/demandware.static/-/Library-Sites-snse-global/default/dw78a6d5db/images/SALE/2024/06_summersale/FR/FR_2/06_SummerSale_BE_FR3_1080x1512.jpg?sw=480&sh=672&q=65'
MINI_APP_URL = 'https://t.me/snipessoldes_bot/snipes'  # Remplace par l'URL de ta mini app

# Fonction pour démarrer le bot et envoyer l'image avec texte et boutons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bot = Bot(token=TOKEN)
    
    user_first_name = update.message.from_user.first_name

    try:
        # Texte du message avec le prénom de l'utilisateur
        message_text = (
            f"Hey {user_first_name}! Inspire-toi des marques les plus tendances du monde, compose tes toutes nouvelles tenues d'été et économise jusqu'à -70% sur les vêtements, sneakers et accessoires !\n\n"
        )

        # Boutons
        keyboard = [
            [InlineKeyboardButton("J'en Profite !", url=MINI_APP_URL)],
            [InlineKeyboardButton("Instagram", url='https://www.instagram.com/snipes/')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Envoi de l'image avec le texte en légende et les boutons
        await bot.send_photo(chat_id=update.message.chat_id, photo=IMAGE_URL, caption=message_text, reply_markup=reply_markup)
        print("Image envoyée avec succès")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
        await update.message.reply_text("Failed to send message.")

def main() -> None:
    # Initialiser l'application avec le token de ton bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Ajouter les gestionnaires
    application.add_handler(CommandHandler('start', start))

    # Démarrer le bot
    application.run_polling()

if __name__ == '__main__':
    main()
