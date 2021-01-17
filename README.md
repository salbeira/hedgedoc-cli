# Dependencies

I guess any python3 version should work. This project uses absolutely no magic or special syntax.

## Libraries

```requests```

Thats it ...

# How to use

You can edit the config.ini file to save yourself some command line arguments. Stuff like the URL of the hedgedoc instance you are communicating with or your personal AUTH-token (when it is implemented) should barely change.

## Arguments / Flags for all commands

### URL

Define the URL of the hedgedoc instance you want to talk to. Can be predefined in the config.ini so you do not have to enter it every time.

```hedgedoc COMMAND --url URL```

### AUTH

Set the AUTH token to be used for this transaction. Not yet implemented as hedgedoc has no authentification yet.

```hedgedoc COMMAND --auth TOKEN```

### VERBOSE

Set the output to verbose.

```hedgedoc COMMAND --verbose```

### SILENT

Silences all informational output.

```hedgedoc COMMAND --silent```

## Commands

The following features are available.

### publish

Publishes a new note contained in the specified file to the hedgedoc instance.

Upload via stdin or text directly as a commandline argument is not yet supported.

```hedgedoc publish --file PATH [--id ALIAS]```

### replace

Replaces the content of an already existing note with the content of the specified file.

```hedgedoc replace --file PATH --id NOTE_ID_OR_ALIAS```

### append

Appends the content of the specified file to an already existing note.

```hedgedoc append --file PATH --id NOTE_ID_OR_ALIAS```

### fetch

Fetches the content of an already existing note and prints it to stdout

```hedgedoc fetch --id NOTE_ID_OR_ALIAS```

### metadata

Fetches the metadata of an already existing note and pretty prints it to stdout.

TODO: Add a -json flag to skip the pretty printing

```hedgedoc metadata --id NOTE_ID_OR_ALIAS```

### permissions

Fetches the permissions of an already existing note and pretty prints it to stdout.

TODO: Add a -json flag to skip the pretty printing

```hedgedoc permissions --id NOTE_ID_OR_ALIAS```

### downlaod

Fetches the content of an existing note and replaces the content of the specified file with the fetched content. Creates the file if it does not yet exist. Obviously, this operation performs changes to your file system and should be used with the usual amount of caution.

```hedgedoc download --file PATH --id NOTE_ID_OR_ALIAS```