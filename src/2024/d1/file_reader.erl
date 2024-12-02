-module(file_reader).
-export([read_file/1]).

read_file(Filename) ->
    case file:read_file(Filename) of
        {ok, Binary} -> Binary;
        {error, Reason} -> io:format("Error reading file: ~p~n", [Reason]), exit(Reason)
    end.


