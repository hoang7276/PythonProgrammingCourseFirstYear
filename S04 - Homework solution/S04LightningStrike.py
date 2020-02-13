# This program calculates the distance to a lightning strike based on the time difference it took to hear the thunder vs see the lightning

def main():
    print("Distance from a lightning strike estimator")
    print("Please enter how many seconds after the lightning was the thunder heard:", end=" ")
    TimeDiff = float(input())
    SoundSpeed = 343
    LightSpeed = 3 * 10**8
    # distance = time * speed, distance is the same so after some calculations:
    LightningTime= TimeDiff*SoundSpeed/(LightSpeed-SoundSpeed)
    Distance = LightSpeed*LightningTime
    print("The distance is ", round(Distance, 2), "meters")


main()
