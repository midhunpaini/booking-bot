from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.select_place_to_go("Goa")
    bot.select_date()
    bot.occupancy()
    bot.search()