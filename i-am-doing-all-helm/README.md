# Wifee Helm Chart

This repository contains the Helm chart for deploying the Wifee application to Kubernetes.

## Chart Structure

```
.
├── charts
│   └── mongodb-15.6.17.tgz
├── templates
│   ├── helpers.tpl
│   ├── certificate.yaml
│   ├── cluster-issuer.yaml
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── secret.yaml
│   ├── service-monitor.yaml
│   └── service.yaml
├── .helmignore
├── Chart.lock
├── Chart.yaml
├── values.yaml
└── README.md

## Prerequisites

- Kubernetes 1.12+
- Helm 3.0+

## Installing the Chart

To install the chart with the release name `my-release`:

```bash
$ helm install my-release .
```

## Configuration

The following table lists the configurable parameters of the Wifee chart and their default values.

| Parameter | Description | Default |
|-----------|-------------|---------|
| `replicaCount` | Number of replicas | `1` |
| `image.repository` | Image repository | `""` |
| `image.tag` | Image tag | `""` |
| `image.pullPolicy` | Image pull policy | `IfNotPresent` |
| `ingress.enabled` | Enable ingress | `false` |
| `service.type` | Kubernetes Service type | `ClusterIP` |
| `service.port` | Kubernetes Service port | `80` |

For more information on the available parameters, please refer to the [values.yaml](values.yaml) file.

## Upgrading

To upgrade the chart:

```bash
$ helm upgrade my-release .
```

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```bash
$ helm delete my-release
```

## Contributing

We welcome contributions to this chart. Please read our [contributing guide](CONTRIBUTING.md) for more information on how to get started.

## License

This Helm chart is licensed under the [MIT License](LICENSE).