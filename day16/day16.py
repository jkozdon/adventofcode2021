import sys
from math import prod

bits_to_num = {
    "0000": 0,
    "0001": 1,
    "0010": 2,
    "0011": 3,
    "0100": 4,
    "0101": 5,
    "0110": 6,
    "0111": 7,
    "1000": 8,
    "1001": 9,
    "1010": 10,
    "1011": 11,
    "1100": 12,
    "1101": 13,
    "1110": 14,
    "1111": 15,
}

char_to_bits = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

bits3_to_num = {
    "000": 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6,
    "111": 7,
}


def parse_sum_packet(bits, idx):
    (vals, idx) = (
        parse_length_type(bits, idx + 1)
        if bits[idx] == "0"
        else parse_num_type(bits, idx + 1)
    )
    return (sum(vals), idx)


def parse_prod_packet(bits, idx):
    (vals, idx) = (
        parse_length_type(bits, idx + 1)
        if bits[idx] == "0"
        else parse_num_type(bits, idx + 1)
    )
    return (prod(vals), idx)


def parse_min_packet(bits, idx):
    (vals, idx) = (
        parse_length_type(bits, idx + 1)
        if bits[idx] == "0"
        else parse_num_type(bits, idx + 1)
    )
    return (min(vals), idx)


def parse_max_packet(bits, idx):
    (vals, idx) = (
        parse_length_type(bits, idx + 1)
        if bits[idx] == "0"
        else parse_num_type(bits, idx + 1)
    )
    return (max(vals), idx)


def parse_literal_packet(bits, idx):
    num = 0
    done = False
    while not done:
        done = bits[idx] == "0"
        num = num * 16 + bits_to_num[bits[idx + 1 : idx + 5]]
        idx += 5
    return (num, idx)


def parse_gt_packet(bits, idx):
    (vals, idx) = (
        parse_length_type(bits, idx + 1)
        if bits[idx] == "0"
        else parse_num_type(bits, idx + 1)
    )
    return (1 if vals[0] > vals[1] else 0, idx)


def parse_lt_packet(bits, idx):
    (vals, idx) = (
        parse_length_type(bits, idx + 1)
        if bits[idx] == "0"
        else parse_num_type(bits, idx + 1)
    )
    return (1 if vals[0] < vals[1] else 0, idx)


def parse_eq_packet(bits, idx):
    (vals, idx) = (
        parse_length_type(bits, idx + 1)
        if bits[idx] == "0"
        else parse_num_type(bits, idx + 1)
    )
    return (1 if vals[0] == vals[1] else 0, idx)


parse_packet_type = [
    parse_sum_packet,
    parse_prod_packet,
    parse_min_packet,
    parse_max_packet,
    parse_literal_packet,
    parse_gt_packet,
    parse_lt_packet,
    parse_eq_packet,
]


def parse_length_type(bits, idx):
    vals = []
    packets_length = parse_number(bits, idx, idx + 15)
    idx += 15
    endx = idx + packets_length
    while idx < endx:
        # packet_version = bits3_to_num[bits[idx:idx+3]]
        idx += 3
        packet_type = bits3_to_num[bits[idx : idx + 3]]
        idx += 3
        (num, idx) = parse_packet_type[packet_type](bits, idx)
        vals.append(num)
    return (vals, idx)


def parse_num_type(bits, idx):
    packets_num = parse_number(bits, idx, idx + 11)
    vals = []
    idx += 11
    while len(vals) < packets_num:
        # packet_version = bits3_to_num[bits[idx:idx+3]]
        idx += 3
        packet_type = bits3_to_num[bits[idx : idx + 3]]
        idx += 3
        (num, idx) = parse_packet_type[packet_type](bits, idx)
        vals.append(num)
    return (vals, idx)


def parse_number(bits, idx, endx):
    num = 0
    for i in range(idx, endx):
        num = 2 * num + int(bits[i])
    return num


def parta(bits):
    idx = 0
    val = 0
    while idx + 6 < len(bits):
        packet_version = bits3_to_num[bits[idx : idx + 3]]
        packet_type = bits3_to_num[bits[idx + 3 : idx + 6]]
        val += packet_version
        idx += 6
        # For part a we can just ignore the length, and
        # just keep searching for the next version info
        if packet_type == 4:
            (num, idx) = parse_literal_packet(bits, idx)
        elif bits[idx] == "0":
            idx += 1 + 15
        else:
            idx += 1 + 11
    print(f"part a: {val}")


def partb(bits):
    idx = 0
    # packet_version = bits3_to_num[bits[idx:idx+3]]
    idx += 3
    packet_type = bits3_to_num[bits[idx : idx + 3]]
    idx += 3
    (num, idx) = parse_packet_type[packet_type](bits, idx)
    print(f"part b: {num}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"python {sys.argv[0]} <string>")
        print("example:")
        print(f"  python {sys.argv[0]} $(cat input.txt)")
    else:
        string = sys.argv[1]
        bits = ""
        for c in string:
            bits += char_to_bits[c]
        parta(bits)
        partb(bits)
