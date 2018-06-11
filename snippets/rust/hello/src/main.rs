extern crate rand;


use std::io;
use std::cmp::Ordering;
use rand::Rng;


fn main() {
    println!("Guess the number");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    //println!("The securet number is {}", secret_number);

    loop {
        println!("Please enter your guess");

        let mut guess = String::new();
        let stdin = io::stdin();

        stdin.read_line(&mut guess)
            .expect("Failed to read line");

        let guess : u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessd: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            },
        };
    }
}
