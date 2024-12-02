-module(main).
-export([main/0]).

main() ->
    Content = file_reader:read_file("input.txt"),
    Lines = string:tokens(Content, "\n"),
    {List1, List2} = lists:foldl(fun(Line, {Acc1, Acc2}) ->
        [Num1, Num2] = string:tokens(Line, "\t "),
        {[Num1 | Acc1], [Num2 | Acc2]}
    end, {[], []}, Lines),
    SortedList1 = lists:sort(List1),
    SortedList2 = lists:sort(List2),
    Differences = lists:zipwith(fun(A, B) ->
        {IntA, _} = string:to_integer(A),
        {IntB, _} = string:to_integer(B),
        abs(IntA - IntB)
    end, SortedList1, SortedList2),
    
    Sum = lists:sum(Differences),
    io:format("~p~n", [Sum]).

