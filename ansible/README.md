## Установка Ansible
Ансайбл лучше ставить из pip (в некоторых дистрибутивах очень старая версия)
```
sudo apt-get install python-pip
sudo pip install ansible
```

## Требования
Нужно сгенерировать ключь для ssh, так как есть шаг распростронения этого ключа (вход без пароля для sysadm)
```
ssh-keygen
```
Также надо иметь возможность sudo либо в inventory прописать ansible_become_pass либо запускать playbook lxc.yml через sudo

## Пример запуска


### Создание LXC контейнеров
Настраивает локальную машину для (устанавливает lxc) а также создает lxc контейнеры с настроенным ssh, пользователем sysadm с правами на sudo
```
ansible-playbook lxc.yaml -i inventory/rlc-local.yaml
```
### Установка ПО
Развернуть стенд c Confluent-kafka и Horton-Hadoop
```
ansible-playbook rlc.yaml -i inventory/rlc-local.yaml
```
