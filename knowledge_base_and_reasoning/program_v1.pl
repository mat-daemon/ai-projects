% semantic network washing machine

washing_machine(brand(siemens), part(X)) :- part(X).

producer(X) :- washing_machine(brand(X), _).

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

problematic_part(X) :- problem(_, part(X), _).


% knowledge base - diagnostic rules

problem(the_door_will_not_open, part(loading_door), reason(safety_function_on)).
problem(the_door_will_not_open, part(loading_door), reason(childproof_lock_on)).
problem(water_is_not_being_pumped_away, part(drain_pump), reason(clogged_drain_pump)).
problem(water_is_not_being_pumped_away, part(water_drain_hose), reason(clogged_water_drain_hose)).
problem(the_program_wont_start, part(loading_door), reason(not_closed_door)).
problem(the_program_wont_start, part(loading_door), reason(childproof_lock_on)).
problem(the_program_wont_start, part(control_panel), reason(start_button_not_pressed)).
problem(drum_briefly_jerks, part(drum), reason(normal)).
problem(water_is_not_visible_in_the_drum, part(drum), reason(normal)).
problem(spin_result_is_not_satisfactory, part(drum), reason(unevenly_distributed_laundry)).
problem(spin_result_is_not_satisfactory, part(drum), reason(selected_speed_too_low)).
problem(leaking_foam, part(loading_door), reason(too_much_detergent_used)).
problem(loud_noises_and_vibrations, part(appliance), reason(appliance_not_level)).
problem(loud_noises_and_vibrations, part(appliance), reason(transit_bolts_not_removed)).
problem(display_panel_do_not_work, part(display_panel), reason(power_down)).
problem(display_panel_do_not_work, part(display_panel), reason(unknown)).
problem(water_is_leaking_from_the_appliance, part(water_drain_hose), reason(water_drain_hose_not_attached)).
problem(water_is_leaking_from_the_appliance, part(water_supply_hose), reason(loose_joint_on_the_water_supply_hose)).
problem(the_appliance_is_not_filling_with_water, part(filter), reason(clogged_filter)).
problem(the_appliance_is_not_filling_with_water, part(water_supply_hose), reason(kinked_water_supply_hose)).



solution(problem(the_door_will_not_open, part(loading_door), reason(safety_function_on)), click_key_button_on_display).
solution(problem(the_door_will_not_open, part(loading_door), reason(childproof_lock_on)), wait_until_programme_ends).
solution(problem(water_is_not_being_pumped_away, part(drain_pump), reason(clogged_drain_pump)), clean_the_drain_pump).
solution(problem(water_is_not_being_pumped_away, part(water_drain_hose), reason(clogged_water_drain_hose)), clean_the_drain_hose).
solution(problem(the_program_wont_start, part(loading_door), reason(not_closed_door)), close_the_door).
solution(problem(the_program_wont_start, part(loading_door), reason(childproof_lock_on)), click_key_button_on_display).
solution(problem(the_program_wont_start, part(control_panel), reason(start_button_not_pressed)), click_start_button).
solution(problem(spin_result_is_not_satisfactory, part(drum), reason(selected_speed_too_low)), change_speed).
solution(problem(leaking_foam, part(loading_door), reason(too_much_detergent_used)), mix_one_tablespoon_of_fabric_softener_with_half_litre_of_water_and_pour_it_into_compartment_II).
solution(problem(loud_noises_and_vibrations, part(_), reason(appliance_not_level)), level_the_appliance).
solution(problem(loud_noises_and_vibrations, part(_), reason(transit_bolts_not_removed)), remove_transit_bolts).
solution(problem(water_is_leaking_from_the_appliance, part(water_drain_hose), reason(water_drain_hose_not_attached)), attach_water_drain_hose).
solution(problem(water_is_leaking_from_the_appliance, part(water_supply_hose), reason(loose_joint_on_the_water_supply_hose)), tighten_joint_on_the_water_supply_hose).
solution(problem(the_appliance_is_not_filling_with_water, part(filter), reason(clogged_filter)), clean_the_filter).
solution(problem(the_appliance_is_not_filling_with_water, part(water_supply_hose), reason(kinked_water_supply_hose)), straighten_the_water_supply_hose).



% reasoning

solvable(X) :- problem(X,Y,Z), solution(problem(X,Y,Z), _).
not_a_fault(X) :- \+ solvable(X).

call_after_sales_service(X) :- problem(X, _, reason(unknown)).
call_after_sales_service(Y) :- \+ problem(Y, _, _).