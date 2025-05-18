# photography-workflow

Requires: distrobox

```
podman build . --tag photography-workflow
distrobox create --image localhost/photography-workflow:latest --name photography-workflow
distrobox enter photography-workflow
```
