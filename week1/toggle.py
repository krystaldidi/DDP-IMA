def toggle_light(light_on):
if light_on:
   light_on = False
   print ("Light turned off.")
else:
   light_on = True
   print ("Light turned on.")
return light_on


toggle_light("")
