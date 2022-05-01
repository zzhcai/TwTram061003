# Requirements:

- Download your `openrc.sh` from MRC, put it under the current directory.

- Generate a password from MRC for OpenStack API access.

- Install `ansible`.

  For other OS distributions, also manually install dependencies `python3-dev`, `python3-setuptools`, and `python3-pip`.

  ```
  # For Linux (Ubuntu) only
  sudo apt-get update && sudo apt-get install -y software-properties-common
  sudo apt-add-repository --yes --update ppa:ansible/ansible
  sudo apt-get install -y ansible
  ```

- Generate a pair of ssh keys:

  ```
  ssh-keygen -t rsa -f cloud.key
  chmod 600 cloud.key
  ```

- Create instances and deploy config related

  ```
  chmod 755 run-mrc.sh
  ./run-mrc.sh
  ```
