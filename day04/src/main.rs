use std::collections::HashSet;
use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file = &args[1];
    let file = fs::read_to_string(file).expect("Should have been able to read the file");

    // Parse boards into number list
    let mut vals = vec![HashSet::<(usize, usize, usize)>::new(); 100];
    let mut totals = vec![0; 0];
    for (iter, line) in file.lines().skip(2).enumerate() {
        let board = iter / 6;
        let row = iter % 6;
        if row == 0 {
            totals.push(0);
        };
        if row < 5 {
            for (col, num) in line.split_whitespace().enumerate() {
                let n: usize = num.parse().expect("parse error");
                vals[n].insert((board, row, col));
                totals[board] = totals[board] + n;
            }
        }
    }

    // Loop through boards and keep track of what has win
    let mut nboards = totals.len();
    let mut board_done = vec![false; nboards];
    let mut scores = vec![0; (5 + 5) * nboards];
    let mut firstwin = 0;
    let mut lastwin = 0;
    'outer: for n in file.lines().nth(0).unwrap().split(',') {
        let n: usize = n.parse().expect("parse error");
        for (board, row, col) in vals[n].iter() {
            let board = *board;
            let row = *row;
            let col = *col;
            if board_done[board] {
                continue;
            }

            totals[board] = totals[board] - n;

            // Handle row value
            let ind = 10 * board + row;
            scores[ind] = scores[ind] + 1;
            if scores[ind] == 5 {
                board_done[board] = true;
            }

            // Handle col value
            let ind = 10 * board + 5 + col;
            scores[ind] = scores[ind] + 1;
            if scores[ind] == 5 {
                board_done[board] = true;
            }

            // Mark board done
            if board_done[board] {
                nboards = nboards - 1;
                if firstwin == 0 {
                    firstwin = totals[board] * n;
                }
                if nboards == 0 {
                    lastwin = totals[board] * n;
                    break 'outer;
                }
            }
        }
    }
    println!("first win: {}", firstwin);
    println!("last win:  {}", lastwin);
}
