import pywhatkit


# Send a WhatsApp Message to a Contact
def send_whatsapp_message(number, message, hours, minutes):
    pywhatkit.sendwhatmsg(number, message, hours, minutes)


# Same as above but Closes the Tab in 4 Seconds after Sending the Message
def send_whatsapp_message_close_tab(number, message, hours, minutes, seconds, tab_close_seconds):
    pywhatkit.sendwhatmsg(number, message, hours, minutes, seconds, True, tab_close_seconds)


# Send an Image to a Group with the Caption as Hello
def send_whatsapp_image(address, image, caption_message):
    pywhatkit.sendwhats_image(address, image, caption_message)


# Send an Image to a Contact with the no Caption
def send_whatsapp_image_with_no_caption(address, image):
    pywhatkit.sendwhats_image(address, image)


# Send a WhatsApp Message to a Group at 12:00 AM
def send_whatsapp_image_to_group(group, message, hours, minutes):
    pywhatkit.sendwhatmsg_to_group(group, message, hours, minutes)


# Send a WhatsApp Message to a Group instantly
def send_whatsapp_image_to_group_instantly(group, message):
    pywhatkit.sendwhatmsg_to_group_instantly(group, message)


# Play a Video on YouTube
def play_video_on_youtube(video):
    pywhatkit.playonyt(video)



# Below are the methods to run

# send_whatsapp_message("+916239229049", "Hi", 23, 25)
# send_whatsapp_message_close_tab("+916239229049", "Hi", 19, 4, 9, 4)
# send_whatsapp_image("IBvnJUkHHEB8QdZfzndtLr", "test_image.jpg", "Test Image")
# send_whatsapp_image_with_no_caption("+916239229049", "test_image.jpg")
# send_whatsapp_image_to_group("IBvnJUkHHEB8QdZfzndtLr", "Test Message", 19, 15)
# send_whatsapp_image_to_group_instantly("IBvnJUkHHEB8QdZfzndtLr", "Test Message")
# play_video_on_youtube("PyWhatKit")