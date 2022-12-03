use std::collections::HashSet;
use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file = &args[1];
    let file = fs::read_to_string(file).expect("Should have been able to read the file");

    // Part 1
    let cnt = file.lines().nth(0).unwrap().len();
    let mut cnt = vec![0; cnt];

    for l in file.lines() {
        for (i, c) in l.chars().enumerate() {
            cnt[i] = cnt[i] + if c == '1' { 1 } else { -1 };
        }
    }

    let mut gamma = 0;
    let mut epsilon = 0;
    let mut base = 1;
    for e in cnt.iter().rev() {
        if *e > 0 {
            gamma = gamma + base;
        } else if *e < 0 {
            epsilon = epsilon + base;
        }
        base = base * 2;
    }

    // Part 2
    let mut ones = HashSet::new();
    let mut zeros = HashSet::new();
    let n = cnt.len();
    for l in file.lines() {
        match l.chars().nth(0) {
            Some('1') => ones.insert(l),
            _ => zeros.insert(l),
        };
    }

    let (mut ox, mut co) = if ones.len() < zeros.len() {
        (zeros, ones)
    } else {
        (ones, zeros)
    };

    // handle oxygen
    for i in 1..n {
        let mut ones = HashSet::new();
        let mut zeros = HashSet::new();
        for l in ox {
            match l.chars().nth(i) {
                Some('1') => ones.insert(l),
                _ => zeros.insert(l),
            };
        }
        ox = if ones.len() < zeros.len() {
            zeros
        } else {
            ones
        };
    }

    // handle co2
    for i in 1..n {
        let mut ones = HashSet::new();
        let mut zeros = HashSet::new();
        for l in co {
            match l.chars().nth(i) {
                Some('1') => ones.insert(l),
                _ => zeros.insert(l),
            };
        }
        co = if ones.len() != 0 && ( zeros.len() == 0 || ones.len() <
                                     zeros.len()) {
            ones
        } else {
            zeros
        };
    }

    let mut ox_num = 0;
    let mut co_num = 0;
    let mut base = 1;
    let ox = ox.iter().nth(0).unwrap();
    let co = co.iter().nth(0).unwrap();
    for c in ox.chars().rev() {
        if c == '1' {
            ox_num = ox_num + base;
        }
        base = base * 2;
    }
    let mut base = 1;
    for c in co.chars().rev() {
        if c == '1' {
            co_num = co_num + base;
        }
        base = base * 2;
    }

    println!("gamma * epsilon: {}", gamma * epsilon);
    println!("oxygen * CO2:    {}", ox_num * co_num);
}
