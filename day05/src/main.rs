use std::cmp::max;
use std::collections::HashSet;
use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file = &args[1];
    let file = fs::read_to_string(file).expect("Should have been able to read the file");

    let mut segments = HashSet::<(i32, i32, i32, i32)>::new();
    let mut xmax = 0;
    let mut ymax = 0;
    for line in file.lines() {
        let v: Vec<i32> = line
            .replace(" -> ", ",")
            .split(',')
            .map(|v| v.parse().unwrap())
            .collect();
        segments.insert((v[0], v[1], v[2], v[3]));
        xmax = xmax.max(max(v[0], v[2]));
        ymax = ymax.max(max(v[1], v[3]));
    }

    xmax = xmax + 1;
    ymax = ymax + 1;
    let mut vh = vec![0; (xmax * ymax) as usize];
    let mut vhd = vec![0; (xmax * ymax) as usize];
    let mut vh_found = 0;
    let mut vhd_found = 0;
    for (x1, y1, x2, y2) in segments {
        let dist = max((x1 - x2).abs(), (y1 - y2).abs()) + 1;
        let xdir = if x1 < x2 {
            1
        } else if x1 > x2 {
            -1
        } else {
            0
        };
        let ydir = if y1 < y2 {
            1
        } else if y1 > y2 {
            -1
        } else {
            0
        };
        for i in 0..dist {
            let x = x1 + i * xdir;
            let y = y1 + i * ydir;
            let ind = (x + xmax * y) as usize;
            if xdir == 0 || ydir == 0 {
                vh[ind] = vh[ind] + 1;
                if vh[ind] == 2 {
                    vh_found = vh_found + 1;
                }
            }
            vhd[ind] = vhd[ind] + 1;
            if vhd[ind] == 2 {
                vhd_found = vhd_found + 1;
            }
        }
    }
    println!("vertical and horizontal: {}", vh_found);
    println!("all directions:          {}", vhd_found);
}
