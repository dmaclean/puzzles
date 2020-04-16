import sys


def is_green(_dist, _speed, _dur):
    """
    Determine if the light is green when the vehicle crosses the segment at a speed.

    Light is green if
    1. we can traverse the entire distance at max speed within one light interval
    2. we can traverse exactly at the end of one light interval

    :param _dist: The distance to traverse for the segment (assumes meters)
    :param _speed: The speed that the vehicle is going (assumes m/s)
    :param _dur: The light duration
    """
    return (_dist / _speed < _dur) or round(_dist / (_speed * _dur), 5) % 2 < 1  # This rounding feels like a hack


def as_km_h(v):
    """
    Convert a speed in m/s to km/h.

    :param v: The m/s speed to convert
    """
    return int(v / 1000 * 3600)


def as_m_s(v):
    """
    Convert a speed in km/h to m/s.

    :param v: The km/h speed to convert
    """
    return (v * 1000) / 3600


def determine_acceptable_speeds(_max_speed, _dur, _dist):
    """
    Determine all speeds from 1 km/h to _max_speed that will get us across the segment during a
    green light.

    :param _max_speed: The maximum speed the car can go.
    :param _dur: The duration of a single light (red --> green or green --> red.
    :param _dist: The distance the car must traverse.
    """
    print(f'max-speed (k/m)={_max_speed}, dur={_dur}, dist={_dist}', file=sys.stderr)
    _speeds = set()
    x = 1  # Start at km/h = 1
    while x < _max_speed:
        # Go through loop iterations until we've exceeded the max speed
        # The inner loop will increment x by the number of seconds in a light iteration
        for i in range(x, x + _dur):
            # I don't know why I made two loops like this, but I don't feel like consolidating at this point.
            # At first I was incrementing x by (2 * dur) to skip red lights, but that got too complicated.
            if i > _max_speed:
                break
            m_s_max = as_m_s(_max_speed)
            m_s = as_m_s(i)  # For evaluating whether light is green at a point in time
            if i + 1 > _max_speed and is_green(_dist, m_s_max, _dur):
                # Add f if it is the max speed and is acceptable.
                # This condition will happen if f is, say 13.8 and i is currently 13, but the next
                # iteration will make i = 14 and and the loop will break
                _speeds.add(_max_speed)
                print(f'Added max speed {_max_speed} km/h ({m_s_max})', file=sys.stderr)
            elif is_green(_dist, m_s, _dur):
                # The light will be green when we are completing the distance.
                print(f'Added {i} km/h ({m_s})', file=sys.stderr)
                _speeds.add(i)
            else:
                # Light will be red - not a candidate speed
                print(f'Skipping {i} km/h ({m_s})', file=sys.stderr)
        x += _dur
    print(f'Speeds for f={_max_speed}, dur={_dur} are {_speeds}', file=sys.stderr)
    return _speeds


def process():
    max_km_h = int(input())
    light_count = int(input())
    segments = []
    for i in range(light_count):
        # Record segment info and print out values for debugging.
        distance, duration = [int(j) for j in input().split()]
        print(f'{distance}/{duration}', file=sys.stderr)
        segments.append([distance, duration])
    speeds = []
    all_speeds = []
    for s in segments:
        # Process each segment and determine all the speeds at which the car will complete
        # the segment during a green light.
        dist = s[0]
        dur = s[1]
        acc_sp = determine_acceptable_speeds(max_km_h, dur, dist)
        speeds.append(acc_sp)
        all_speeds.extend(acc_sp)
    print(f'Speeds (km/h) is {[v for v in all_speeds]}', file=sys.stderr)

    # Create a big set of all the acceptable speeds for all lights for AND-ing purposes
    common = {s for s in all_speeds}
    print(f'Common starts as {common}', file=sys.stderr)
    for s in speeds:
        # Go through each set of acceptable speeds and AND them against the common set.
        # Since the common set contains all speeds that were acceptable for ANY segment, it
        # will retain the ones that are common and drop the ones that aren't in
        # at least this current segment.
        # After the last segment is processed, we'll have a set of all speeds that will allow
        # the car to cross ALL segments at a green light.  Then it's just a matter of finding the max.
        print(f'Stretch has {s}', file=sys.stderr)
        common &= s
        print(f'Common now has {common}', file=sys.stderr)
    print(f'Using {min(speeds)}', file=sys.stderr)
    # Print out our answer - the maximum value of what's left in the common set.
    print(max(common))


if __name__ == '__main__':
    process()
