def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello World!'

    if message == '/info':
        return 'Hi!, I am Resolution Assistant Bot. Here to help you to complete your New year Resolutions.'

    if p_message == '/help':
        return ('Here are the commands you can use:'
                '\n `/new_year_resolution`: To add a new year resolution.'
                '\n `/list`: To list all the resolutions.'
                '\n `/delete`: To delete a resolution.'
                '\n `/update`: To update a resolution.'
                '\n `/suggest`: To get suggestions for a resolution.'
                '\n `/goal_achieved`: To mark a resolution as achieved.'
                '\n `/eco_points`: To check how many eco points you have achieved.'
                '\n `/remind_me`: To set a reminder for a resolution.'
                '\n `/reedem`: To reedem eco points for a reward.'
                )

    return 'I didn\'t understand what you wrote. Try typing "/help".'