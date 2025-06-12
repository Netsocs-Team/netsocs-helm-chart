# Netsocs Helm Chart

This is the official Helm chart for Netsocs Kubernetes deployments.

## Installation

To install the Netsoc Helm chart, add the Netsocs Helm repository to your Helm installation:

```bash
helm repo add netsocs https://netsocs.github.io/helm-charts
```

Then, you can install the chart using the following command:

```bash
helm install netsocs/netsocs
```

## Services and modules
- [x] Dashboard backend
- [x] Dashboard frontend
- [x] Auth UI
- [ ] Auth backend
- [ ] Event Service
- [x] Event logs backend
- [x] Event logs frontend
- [x] Device management
- [x] Video widget frontend
- [ ] Video widget backend: This backend use the path `/api/netsocs/module.video/` in the API Gateway.
- [ ] Video service
- [ ] Live video engine
- [ ] Playback video engine
- [ ] DriverHUB
- [ ] Configuration backend
- [ ] Configuration frontend
- [ ] Redis
- [ ] Kafka
- [ ] Database
- [ ] Synoptic frontend
- [ ] Synoptic backend
- [ ] KPI frontend
- [ ] KPI backend
- [ ] Corporation backend
- [ ] Corporation frontend
- [ ] Reports frontend
- [ ] Reports backend
- [ ] Employee frontend
- [ ] Employee backend
