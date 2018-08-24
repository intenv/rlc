# Пример запуска

## Создание LXC контейнеров
Настраивает локальную машину для (устанавливает lxc) а также создает lxc контейнеры с настроенным ssh, пользователем sysadm с правами на sudo
```
ansible-playbook lxc.yaml -i inventory/rlc-local.yaml
```
## Установка ПО
Развернуть стенд c Confluent-kafka и Horton-Hadoop
```
ansible-playbook rlc.yaml -i inventory/rlc-local.yaml
```
