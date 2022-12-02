use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file = &args[1];
    let file = fs::read_to_string(file).expect("Should have been able to read the file");

    let mut depth1 = 0;
    let mut depth2 = 0;
    let mut horz = 0;
    let mut aim = 0;

    for line in file.lines() {
        let tok: Vec<&str> = line.split(' ').collect();
        let val: u32 = tok[1].trim().parse().expect("Wanted a number");
        if tok[0] == "up" {
            aim = aim - val;
            depth1 = depth1 - val;
        } else if tok[0] == "down" {
            aim = aim + val;
            depth1 = depth1 + val;
        } else if tok[0] == "forward" {
            horz = horz + val;
            depth2 = depth2 + val * aim;
        } else if tok[0] == "backward" {
            horz = horz - val;
            depth2 = depth2 - val * aim;
        }
    }

    println!("product part 1: {}", depth1 * horz);
    println!("product part 2: {}", depth2 * horz);
}
