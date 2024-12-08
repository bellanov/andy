# Kubernetes

Kubernetes is a technology used to orchestrate, schedule, and manage containers (i.e., Docker).

Below is an overview of the design patterns to be utilized within **Kubernetes**.

Review for your own knowledge, as this is the reality we will be coding towards.

# Multi-Container Patterns

Diving into well-known **multi-container** _practices_ / _patterns_.

## Pods

An extra level of **abstraction**, above _containers_.

- Allow you to specify _additional information_ beyond containers.
  - Restart Policies / Init Containers
  - Probes ( readiness, liveness )
- Simplifies using different container _runtimes_ (Python, NodeJS, RUST, etc.).
- Co-locate **tightly coupled** containers without _packaging_ them as a _single unit_.
  - Solves unnecessary dependencies issue and keeps containers lean.
  - Can have _multiple pods_ collocated and operating as a **single unit**.
    - Don't need to package them as a _single image_.

## Sidecar Pattern

- Uses a _helper_ container to assist a _primary_ container.
- Commonly used for _logging_, _file syncing_, _watchers_.
- Benefits include _leaner main container_, _failure isolation_, and _independent update cycles_.
  - Adding additional useful functionality via a sidecar, rather than burdening the main container with additional responsibilities.

### File Sync Sidecar Example

In this example, the **primary** container is the _Web Server_ and the **sidecar** is the _Content Puller_.

- **Primary Container:** Web Server
- **Sidecar:** Content Puller
- _Content Puller_ syncs with _Content Management System (CMS)_.
  - Pulls files for the _Web Server_ to serve.
- _Web Server_ serves content.
- The content is _synced_ using a **Volume**. 

![Image](https://github.com/user-attachments/assets/cc8f7364-d2c9-4aee-a9f9-3ac8ed57d686)

## Ambassador Pattern

- **Ambassador** container is a _proxy_ for communicating to and from the **primary** container.
- Commonly used for communicating with **databases**.
  - The application can be configured to always connect to **_localhost_**.
  - Responsibility of connectivity to the right database is given to the **_ambassador_**.
  - In _Prod_ environments, the _ambassador_ can be configured to work with _sharded_ databases as well. 
  - **Application** in the _primary_ container only needs to consider a _single logical database_, accessible over **localhost** (naturally via Pod).
- Streamlined development experience, potential to **_reuse_** of the ambassador across multiple languages.
  - Can run a **local** database on your machine without requiring the **ambassador**.

### Database Ambassador Example

In this example, the **primary** container is the _Web App_ and the **ambassador** container is the _Database Proxy_.

- Database _requests_ are sent to the _Database Proxy_ over **localhost**.
- _Database Proxy_ then **forwards** the requests to the appropriate database.
- Possibly _sharding_ the requests.
- Web App is free from any of the associated complexity.

![Image](https://github.com/user-attachments/assets/53861ad8-57a0-4763-ab31-7a637daf3c63)

## Adapter Pattern

- Uses a _container_ to present a **standardized interface** across multiple _Pods_
  - **EXAMPLE:** Presenting an interface for accessing output in a standard format for logs across several applications
- Opposite of the **Ambassador** pattern.
  - **Ambassador** presents a _simplified view_ of the **primary** container.
  - **Adapter** presents a _simplified view_ of the **application** to the outside world.
- Commonly used for **normalizing** _output logs_ and _monitoring data_  that can easily be consumed by a shared aggregation system.
  - Can communicate with the **primary** container using either a _shared volume_ when dealing with **files** or over **localhost** (i.e., getting metric data from a REST API).
- "Adapts" third-party software to meet your needs.
  - Adapt an application's output without requiring code changes.
  - May be required if you don't have access to an application's source code.
    - Even with access to the source, this is a much cleaner solution.
    - Don't burden the application with additional complexity.

### Adapter Pattern Demo

A demo of how to implement the Adapter pattern. The demo uses a _Pretend Legacy App_ to exemplify the concepts. 

- Outputs log data in a _raw_, _archaic_ format, hence **legacy**.
- Date, CPU, and memory information is being exported.

#### Pretend Legacy App

```sh
while true; do
  date > /metrics/raw.txt
  top -n 1 -b >> /metrics/raw.txt
  sleep 5;
```

**PROBLEM:** The _logs_ can't readily be consumed by the _log aggregation system_.

- Monitoring solution likely requires **JSON** data.
  - Current _output_ involves **raw** data from **CLI** commands.

Viewing contents of the logs.

```sh
kubectl exec -n legacy app -- cat /metrics/raw.txt
```

- Monitoring system only interested in...
  - Date
  - Memory
  - User CPU %
  
 The **primary** container shares storage using a _volume_ and the **adapter** presents an _adapted_ view of the raw metric data.

- Metrics will then be represented in JSON.

**SOLUTION:** Adapter container to "adapt" the legacy output to a standard monitoring format.

- Utilize a _volumeMount_ to establish communication between **primary** container and **adapter**.
- **App** mounts a volume at **/metrics/** so that the raw _metrics_ can be _shared_ with the adapter container at **/metrics/raw.txt**.
- **Adapter** container _mounts_ the same _volume_, enabling the containers to share data.
- Utilize a combination of **head** and **tail** to tie things together.
  - _head_ : print out N lines
  - _tail_ : look at the end of the file for N lines
- Isolate the values you care about and export them into an adapted view at **/metrics/adapted.json** 
 - This output is ready for consumption by log aggregation services.