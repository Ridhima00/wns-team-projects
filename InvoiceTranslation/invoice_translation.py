from googletrans import Translator


def translate_invoice(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


# Example usage
if __name__ == "__main__":
    # Sample text in Spanish
    invoice_text = "Factura No. 12345, Fecha: 01/08/2024, Importe Total: 1500 EUR"

    # Translate to English
    translated_text = translate_invoice(invoice_text)

    print("Original Invoice Text:", invoice_text)
    print("Translated Invoice Text:", translated_text)
