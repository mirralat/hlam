(* Awesome! *)

val x = 34;
(* dynamic environment: x --> 34 *)

val y = 17;
(* dynamic environment: y --> 17 *)

val z = (x + y) + (y + 2);
(* dynamic environment: z --> 70 *)

val q = z + 1;
(* dynamic environment: q --> 71 *)

val abs_of_z = if z < 0 then 0 - z else z; (* bool *)
(* abs_of_z: int *)
(* dynamic environment: ..., abs_of_z --> 70 *)

val abs_of_z_simpler = abs(z);