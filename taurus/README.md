## Comandado docker windows - poweshell

```
docker run --rm -it -v ${PWD}:bzt-configs blazemeter/taurus taurus.yaml
```

## Comandado docker windows - CMD

```
docker run --rm -it -v %cd%:bzt-configs blazemeter/taurus taurus.yaml
```

## Comandado docker Linux/MacOS

```
docker run --rm -it -v $(pwd)::bzt-configs blazemeter/taurus taurus.yaml
```
