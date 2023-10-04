fun sum_list (xs : int list) = 
  if null xs
  then 0
  else hd xs + sum_list(tl xs)

fun countdown (x : int) = (* [7, 6, 5, 4, 3, 2, 1] *)
  if x=0
  then []
  else x :: countdown(x-1)

(* (int list) * (int list) -> int list *)
fun append (xs : int list, ys : int list) = 
  if null xs
  then ys
  else (hd xs) :: append((tl xs), ys)

fun sum_pair_list (xs : (int * int) list) = 
  if null xs
  then 0
  else #1 (hd xs) + #2 (hd xs) + sum_pair_list(tl xs)

(* [3, 5] *)
fun firsts (xs : (int * int) list) = 
  if null xs
  then []
  else #1 (hd(xs)) :: firsts(tl xs)

fun seconds (xs : (int * int) list) = 
  if null xs
  then []
  else #2 (hd(xs)) :: seconds(tl xs)

val it = [1, 2, 3, 4]
val data = sum_list it;
countdown 8;

(* functions over pairs of list *)
append([1, 2], [3, 4]);

(* sum_pair_list [(3, 4),(5, 6)] *)
sum_pair_list [(3, 4),(5, 6)];
firsts [(3, 4),(5, 6)];