extern crate rand;

use std::io;
use std::cmp::Ordering;  // Orderingトレイトをスコープに含ませる
use rand::Rng;  // rand::thread_rng()のメソッドを使うにはRngトレイトをスコープに含ませる必要があるらしい


fn main() {
    // start.
    println!("Guess the number!");

    // generate rand.
    let secret_number = rand::thread_rng().gen_range(1,101);

    // println!("The secret number is: {}", secret_number);

    loop {
        println!("Please input your guress.");

        let mut guess = String::new();

        // read_line(): 一行の標準入力を読み込む
        // expect(): エラー発生時、エラーメッセージを表示してPanic!させる（クラッシュさせる）
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        // trim(): 前後の空白や、改行コード（\n）を削除する
        // parse(): 文字列を何らかの数値へとパースする
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,  // Okは成功。parse()に成功した値をnumとして、=>でそのままnumを返している
            Err(_) => continue,  // Errは失敗。名前は適当に_として、失敗時はループをcontinueしている
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {  // 引数に比較対象の参照を指定する
            Ordering::Less    => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal   => {
                println!("You win!");
                break;
            }
        }
    }

}
