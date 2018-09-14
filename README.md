# DevIP

Find a suitable IP host to access local network-based applications.

Inspired on [dev-ip](https://github.com/shakyShane/dev-ip) by @shakyShane.

## Installation

```
pip install dev-ip
```

## Usage

```
$ devip --help
Usage: devip [OPTIONS]

  Find a suitable IP host to access local network-based applications.

Options:
  -a, --all       List all IP addresses.
  -r, --reverse   List in reverse order.
  -l, --loopback  Include loopback.
  --help          Show this message and exit.
```

## Examples

```
$ devip
192.168.1.45
```

```
$ devip -la
127.0.0.1
192.168.1.45
```

```
python -m http.server --bind $(devip)
```
