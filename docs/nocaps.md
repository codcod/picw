# Remap Caps to Ctrl in Windows

If you want to turn your Caps Lock into Ctrl key open `regedit` and go to

    HKEY_LOCAL_MACHINE
    +- SYSTEM
       +- CurrentControlSet
          +- Control
             +- Keyboard Layout

and add a new binary value `Scancode Map` (or edit the existing one). Enter
the following values:

    00 00 00 00
    00 00 00 00
    02 00 00 00
    1d 00 3a 00
    00 00 00 00

Line 4 means: send left Ctrl (0x001d) when pressing Caps Lock (0x003a).

Or save the following as `nocaps.reg` and run it:

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]
"Scancode Map"=hex:00,00,00,00,00,00,00,00,02,00,00,00,1d,00,3a,00,00,00,00,00
```

## Swap instead of disable

If you want to swap Caps with Ctrl rather then disabling it use those values
instead:

    00 00 00 00
    00 00 00 00
    03 00 00 00
    1d 00 3a 00
    3a 00 1d 00
    00 00 00 00

