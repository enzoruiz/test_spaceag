# Test Space AG

## Puesta en Marcha

```
docker-compose up -d --build
```

## Tests

### Inside docker container
```
docker exec -ti ID_CONTAINER bash
pytest
```

### Local
```
pytest
```
