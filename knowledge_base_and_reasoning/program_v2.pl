% semantic network washing machine


washing_machine(brand('siemens iQ500 WM14N121'), Parts) :- findall(P, part(P), Parts).


part(appliance).
part(main_cable).
part(water_drain_hose).
part(water_supply_hose).
part(drain_pump).
part(detergent_drawer).
part(control_panel).
part(loading_door).
part(service_flap).
part(filter).
part(drum).
part(X) :- control_panel_part(X).

control_panel_part(selector).
control_panel_part(display_panel).



% knowledge base - diagnostic rules

problem(the_door_will_not_open).
problem(water_is_not_being_pumped_away).
problem(the_program_wont_start).
problem(drum_briefly_jerks).
problem(water_is_not_visible_in_the_drum).
problem(spin_result_is_not_satisfactory).
problem(leaking_foam).
problem(loud_noises_and_vibrations).
problem(display_panel_do_not_work).
problem(water_is_leaking_from_the_appliance).
problem(the_appliance_is_not_filling_with_water).

        
reason(safety_function_on, the_door_will_not_open).
reason(childproof_lock_on, the_door_will_not_open).
reason(clogged_drain_pump, water_is_not_being_pumped_away).
reason(clogged_water_drain_hose, water_is_not_being_pumped_away).
reason(not_closed_door, the_program_wont_start).
reason(start_button_not_pressed, the_program_wont_start).
reason(unevenly_distributed_laundry, spin_result_is_not_satisfactory).
reason(selected_speed_too_low, spin_result_is_not_satisfactory).
reason(too_much_detergent_used, leaking_foam).
reason(appliance_not_level, loud_noises_and_vibrations).
reason(transit_bolts_not_removed, loud_noises_and_vibrations).
reason(power_down, display_panel_do_not_work).
reason(water_drain_hose_not_attached, water_is_leaking_from_the_appliance).
reason(loose_joint_on_the_water_supply_hose, water_is_leaking_from_the_appliance).
reason(clogged_filter, the_appliance_is_not_filling_with_water).
reason(kinked_water_supply_hose, the_appliance_is_not_filling_with_water).
reason(unknown, _).


related_part(safety_function_on, loading_door).
related_part(childproof_lock_on, loading_door).
related_part(clogged_drain_pump, drain_pump).
related_part(clogged_water_drain_hose, water_drain_hose).
related_part(not_closed_door, loading_door).
related_part(start_button_not_pressed, control_panel).
related_part(unevenly_distributed_laundry, drum).
related_part(selected_speed_too_low, drum).
related_part(too_much_detergent_used, loading_door).
related_part(appliance_not_level, appliance).
related_part(transit_bolts_not_removed, appliance).
related_part(power_down, display_panel).
related_part(water_drain_hose_not_attached, water_drain_hose).
related_part(loose_joint_on_the_water_supply_hose, water_supply_hose).
related_part(clogged_filter, filter).
related_part(kinked_water_supply_hose, water_supply_hose).


solution(safety_function_on, click_key_button_on_display).
solution(childproof_lock_on, wait_until_programme_ends).
solution(clogged_drain_pump, clean_the_drain_pump).
solution(clogged_water_drain_hose, clean_the_drain_hose).
solution(not_closed_door, close_the_door).
solution(childproof_lock_on, click_key_button_on_display).
solution(start_button_not_pressed, click_start_button).
solution(selected_speed_too_low, change_speed).
solution(too_much_detergent_used, mix_one_tablespoon_of_fabric_softener_with_half_litre_of_water_and_pour_it_into_compartment_II).
solution(appliance_not_level, level_the_appliance).
solution(transit_bolts_not_removed, remove_transit_bolts).
solution(water_drain_hose_not_attached, attach_water_drain_hose).
solution(loose_joint_on_the_water_supply_hose, tighten_joint_on_the_water_supply_hose).
solution(clogged_filter, clean_the_filter).
solution(kinked_water_supply_hose, straighten_the_water_supply_hose).
solution(unknown, call_sales_service).


% reasoning

is_this_a_problem(X) :- problem(X).

problematic_part(X) :- problem(Y), reason(Z, Y), related_part(Z, X).

problems_related_to_part(X, Y) :- problem(Y), reason(R, Y), related_part(R, X).

all_problems(Problems) :- findall(P, problem(P), Problems).

solvable(X) :- problem(X), reason(Y, X), solution(Y, _), not(Y=unknown).

is_this_a_fault(X) :- problem(X), reason(Y, X), not(Y=unknown).

problem_reasons(X, Reasons) :- findall(R, reason(R,X), Reasons).

solutions(X, Solutions) :- findall(S, solution(X, S), Solutions).


% interface
start :- washing_machine(brand(Brand), Parts), all_problems(Problems),
    write('Welcome to Logical Serviceman'), nl,
    write('The washing machine is: '),
    write(Brand), nl, nl,
    write(' The washing machine consists of the following parts: '),
    write(Parts), nl, nl,
    write('Potential problems: '),
    write(Problems), nl, nl,
    write('You can do following operations: '), nl,
    write('is_this_a_problem(Problem)'), nl,
    write('is_this_a_fault(Problem)'), nl,
    write('problem_that_is_not_a_fault'), nl,
    write('solvable(Problem)'), nl,
    write('what_caused_a_problem(Problem)'), nl,
    write('how_to_solve(Reason)'), nl,
    write('is_the_part_problematic(Part)'), nl,
    write('problems_related_to_part(Part, P)').

what_caused_a_problem(X) :- problem_reasons(X, Reasons), 
    write(Reasons).

how_to_solve(X) :- solutions(X, Solutions),
    write(Solutions).

is_the_part_problematic(X) :- problematic_part(X).

problem_that_is_not_a_fault :- write('It is a normal behaviour.').
