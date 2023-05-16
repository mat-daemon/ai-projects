start
is_this_a_problem(the_door_will_not_open)
is_this_a_fault(the_door_will_not_open)

is_this_a_problem(drum_briefly_jerks)
is_this_a_fault(drum_briefly_jerks)
% it may happen that something looks like it does not work correct but it is a normal behaviour
problem_that_is_not_a_fault		

solvable(the_door_will_not_open)
what_caused_a_problem(the_door_will_not_open)
how_to_solve(safety_function_on)
% something works wrong, but the reason is not in the list
how_to_solve(unknown)
	
is_the_part_problematic(water_drain_hose)
is_the_part_problematic(main_cable)

problems_related_to_part(water_drain_hose, P)

part(wing)
control_panel_part(selector), part(selector)