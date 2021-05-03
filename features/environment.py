
def before_scenario(context, scenario):
    print("before_scenario")
    #context.driverAndroid = basepage.get_driver_android()

def after_scenario(context, scenario):
    print("after_scenario")
    #context.driverAndroid.quit()