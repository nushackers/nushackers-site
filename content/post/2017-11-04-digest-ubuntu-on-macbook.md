---
author: Johannes Choo
categories:
- Digest
date: 2017-11-03T00:00:00Z
title: 'Digest: Installing and Running Ubuntu 17.10 Desktop on the 12-inch MacBook'
tags: [ubuntu, macbook, linux]
url: /2017/11/03/digest-ubuntu-on-macbook/
---

# Introduction

Not liking macOS? Prefer linux? In this post we'll show you how.

## Requirements

You should have a USB Hub or similar with enough ports for

* One LiveUSB
* One USB Storage Device fast enough to run an OS from (e.g. SanDisk
  Ultra Fit); we shall call this the target device from here on.
* One input device (USB keyboard and mouse required; for ease two
  ports recommended)


As well as a MacBook running a macOS version between El Capitan and
High Sierra (inclusive).

You should be comfortable running commands on terminal; `bash` is
assumed.

## Caveats

* Internal speaker and headphone jack output is still not working
  (probably).
* Chaining GRUB2 bootloader probably needs to be manually (possibly
  automatable) rebuilt every kernel update, and probably the keyboard
  and touchpad drivers too.
* Seems like installing GRUB2 adds a folder to the internal SSD's EFI
  partition that may mess with the MacBook's native bootloader's
  bootable-partition discovery process and its BOOTCAMP bootloading
  process. This is not a major issue as
  * The bootloading process where one holds the `Option` key and
    chooses which volume to boot into still works fine,
  * Booting into Windows through GRUB2 is possible,
  * Removing the `ubuntu` folder from the EFI Partition, resetting the
    default boot partition from macOS, and not connecting the external
    drive containing Ubuntu should revert things to a normal state.
* I strongly do not recommend installing Ubuntu to the internal drive
  as macOS upgrades tend to assume several things about the
  partitioning state of the internal SSD and messing around with it
  outside of Disk Utility and the Bootcamp-proscribed instructions may
  mess stuff up. In particular, note the macOS upgrades that converted
  HFS+ partitions so that they were within CoreStorage partitions, and
  the macOS upgrades that converted HFS+ filesystems into APFS
  filesystems.

## The Stages

1. Preparing the LiveUSB.
  * After this stage you should have a USB containing a live image
that you can boot into from your MacBook
2. Preparing the target device to make it bootable.
  * After this stage you should have a partition that your MacBook
    recognizes as a partition containing macOS that it can boot into.
3. Installing Ubuntu to the target device.
  * After this stage you should have an Ubuntu installation in your
    target device that might not be bootable into.
4. Installing the bootloader.
  * After this stage you should be able to boot into the Ubuntu
    installation, but keyboard and mouse support may not be present.
5. Installing and configuring internal keyboard and touchpad drivers.
  * After this stage your Ubuntu should have internal keyboard and
    touchpad support, but it may no longer be bootable.
6. Rebuilding and reinstalling the bootloader.
  * After this stage you should be able to boot into the Ubuntu
    installation and be able to use your mouse and keyboard.
  * This stage is similar to Stage 4, and I think it must be
    re-performed everytime you update the kernel of your installation.

## Stage 1: Preparing the LiveUSB

1. Download the Ubuntu 17.10 x86_64 Desktop image. I have not tried
   the other versions, which may have slightly different installation
   instructions in stage 3. The 17.10 Beta 2 desktop image suffices.
2. We convert the `.iso` image file into a `.dmg` disk image file that the
   MacBook recognizes as bootable.
   ```
   hdiutil convert -format UDRW -o /path/to/img.dmg /path/to/image.iso
   ```
3. We insert our Live-USB-to-be confirm the location our LiveUSB-to-be
   is at with
   ```
   diskutil list
   ```

   It should be identified by a name of the form `diskN` for some
   integer `N`. Then ensure that none of the partitions present on the
   disk are mounted with
   ```
   diskutil unmountDisk /dev/diskN
   ```
4. We now burn the `.dmg` file to the disk with
   ```
   sudo dd if=/path/to/img.dmg of=/dev/rdiskN
   ```

   Note that writing to `rdiskN` is speedier than writing to `diskN`
   as it skips several layers of software abstraction. Nevertheless,
   depending on the USB standard your LiveUSB supports, it may still
   take quite a while.

We are done with this stage. Unmount your LiveUSB.

## Stage 2: Preparing the Target Device to Make It Bootable

1. Insert the target device. Let `diskN` be its identifier; as before,
   we may discover its identifier with `diskutil list`.
2. Erase the disk, write a GPT and EFI partition and a Journaled HFS+ partition
   to it with
   ```
   diskutil eraseDisk JHFS+ Ubuntu GPT diskN
   ```
3. Split the JHFS partition into a 128MB (size is pretty arbitrary;
   ex. we have used MB and not MiB) partition for the GRUB2 bootloader
   and a partition for our installation with a command like
   ```
   diskutil splitPartition diskNs2 2 JHFS+ "Ubuntu Boot Loader" 128M ExFAT "Ubuntu" R
   ```
4. We now mount the "Ubuntu Boot Loader" partition and navigate our
   terminal shell into its root; the standard Finder mounting
   suffices, whereupon it will be located at `/Volumnes/Ubuntu Boot
   Loader`.
5. We create the necessary folders necessary for the MacBook to
   recognize it as a macOS installation
   ```
   mkdir mach_kernel
   mkdir -p System/Library/CoreServices
   ```
6. We create a `.plist` text file at
   `System/Library/CoreServices/SystemVersion.plist` with the contents
   ```
   <xml version="1.0" encoding="utf-8"?>
   <plist version="1.0">
   <dict>
       <key>ProductBuildVersion</key>
       <string></string>
       <key>ProductName</key>
       <string>Linux</string>
       <key>ProductVersion</key>
       <string>Ubuntu Linux</string>
   </dict>
   </plist>
   ```
7. Finally, we set the boot flag for the partition with
   ```
   sudo bless --device /dev/diskNsM
   ```
   where `M` is the partition identifier of the "Ubuntu Boot Loader"
   partition, which can be discovered with `diskutil list`.

We are done. Insert the LiveUSB and shutdown or restart the MacBook.

## Stage 3: Installing Ubuntu

We assume that the LiveUSB and the target device are both plugged in,
and that the reader shall connect external input devices whenever
required for input.

1. When the MacBook starts, immediately during or before the bootup
   chime, hold down the `Option` button to enter the native
   bootloader. Select any of the `EFI Boot` options.
2. You should boot into the LiveUSB's GRUB2 bootloader. Select "Try
   Ubuntu without installing". Your internal keyboard still works in
   the GRUB2 bootloader
3. You should arrive at the Live Ubuntu desktop. You should need an
   external keyboard and mouse while in this environment. Proceed with
   installation as per usual, except for the following part.
4. At "Installation type", and presented with where and how on the
   disks you wish to install Ubuntu, select "Something else". I do not
   like connecting to the Internet and updating just yet; we may do
   that later.
5. Select to format the partition that was `diskNsM` in macOS as
   `ext4`, and use it as the root `/` mount point. Choose to install
   the bootloader in the same partition, that is, the partition that
   was `diskNsM` in macOS. Leave every other partitions and drives
   alone.
6. Proceed and complete the installation, but do not reboot just yet.

## Stage 4: Making Ubuntu bootable

You should now be booted into a Live Ubuntu OS. You should have both
the LiveUSB connected from which you are running the OS, and also have
your target device connected. We shall identify the partition that you
have installed Ubuntu 17.10 to by `sdAN` where `A` is some small-caps
letter and `N` is some integer.

We now build the GRUB2 bootloader.

1. We mount the Ubuntu 17.10 partition. It suffices to use GNOME's
   default mounting, whereupon it will be availabe at some location
   like `/media/ubuntu/some_uuid_string/`
1. We bind our Live Ubuntu's special files so that they are available when we
   `chroot` into our Ubuntu 17.10 installation with
   ```
   cd /media/ubuntu/some_uuid_string/
   sudo mount -B /dev dev
   sudo mount -B /dev/pts dev/pts
   sudo mount -B /proc proc
   sudo mount -B /sys sys
   sudo mount -B /run run
   ```
2. We `chroot` into our Ubuntu 17.10 installation with
   ```
   sudo chroot .
   ```
3. We configure GRUB2 with
   ```
   grub-mkconfig -o boot/grub/grub.cfg
   ```
4. We build GRUB2 into a `boot.efi` located at the root of our Ubuntu
   17.10 installation with
   ```
   grub-mkstandalone -o boot.efi -d usr/lib/grub/x86_64-efi -O x86_64-efi --compress=xz boot/grub/grub.cfg
   ```
5. From outside the `chroot`'d shell (that is, from the Live Ubuntu
   desktop), save your boot.efi file somewhere from your macOS
   installation (e.g. Google Drive).
6. Reboot into macOS. Due to how the macOS searches for bootable
   partitions, from now on you may have to always hold down the
   `Option` button and select the location you would like to boot
   into, else you may arrive at a GRUB2 fallback shell.
7. Mount the "Ubuntu Boot Loader" partition. From the Terminal,
   (Finder glitches out) copy the GRUB2 image into the partition with
   ```
   cp /path/to/boot.efi "/Volumes/Ubuntu Boot Loader/System/Library/CoreServices/"
   ```
8. It does not seem likely, but you may have to re-bless the "Ubuntu
   Boot Loader" partition.

We are done. Your Ubuntu 17.10 installation should now be bootable.

## Stage 5: Building, configuring, and installing the keyboard and touchpad drivers

You do not need the LiveUSB from here on. Reboot the MacBook with
`Option` key held down while booting, and select "Ubuntu Boot Loader".
You should boot into GRUB2, and should be able to select an Ubuntu
menu entry to boot onto your Ubuntu 17.10 installation. From here on
you may need to perform input via an external keyboard and mouse. Log
in.

1. Connect to the Internet.
2. Update your package lists and then update your system (upgrade)
   with
   ```
   sudo apt update
   sudo apt upgrade
   ```

   You may be prompted to restart your system, but it is important not
   to just yet.
3. Install git and the build tools you will need with
   ```
   sudo apt install git build-essential
   ```
4. Download the experimental keyboard and touchpad drivers with
   ```
   git clone https://github.com/roadrunner2/macbook12-spi-driver
   ```
5. Build the drivers as kernel modules
   ```
   cd macbook12-spi-driver
   git checkout touchbar-driver-hid-driver
   make
   ```
6. Install the kernel modules
   ```
   sudo mkdir /lib/modules/`uname -r`/custom/
   sudo cp applespi.ko appletb.ko /lib/modules/`uname -r`/custom/
   sudo depmod
   ```
7. Write a configuration file to set the touchpad to an appropriate
   DPI. The file should be located at `/etc/udev/hwdb.d/61-evdev-local.hwdb`
   and its contents should be
   ```
   # MacBookPro13,* (Late 2016), MacBookPro14,* (Mid 2017)
   evdev:name:Apple SPI Touchpad:dmi:*:svnAppleInc.:pnMacBookPro13,1:*
   evdev:name:Apple SPI Touchpad:dmi:*:svnAppleInc.:pnMacBookPro13,2:*
   evdev:name:Apple SPI Touchpad:dmi:*:svnAppleInc.:pnMacBookPro14,1:*
   evdev:name:Apple SPI Touchpad:dmi:*:svnAppleInc.:pnMacBookPro14,2:*
    EVDEV_ABS_00=::96
    EVDEV_ABS_01=::94
    EVDEV_ABS_35=::96
    EVDEV_ABS_36=::94

   evdev:name:Apple SPI Touchpad:dmi:*:svnAppleInc.:pnMacBookPro13,3:*
   evdev:name:Apple SPI Touchpad:dmi:*:svnAppleInc.:pnMacBookPro14,3:*
    EVDEV_ABS_00=::96
    EVDEV_ABS_01=::95
    EVDEV_ABS_35=::96
    EVDEV_ABS_36=::95
   ```
8. We configure the modules to load on boot with
   ```
   sudo su
   echo 'add_drivers+="applespi intel_lpss_pci spi_pxa2xx_platform appletb"' >> /etc/initramfs-tools/modules
   update-initramfs -u
   ```

You should now have a system that should load the drivers upon boot.
But (I'm unsure about this point) you may have to rebuild your GRUB2
bootloader to correctly identify the kernel to boot into.

## Stage 6: Rebuilding the GRUB2 Bootloader

After every system update (upgrade) that rebuilds the kernel, you
should re-run this step.

1. Reconfigure GRUB2.
   ```
   sudo grub-mkconfig -o /boot/grub/grub.cfg
   ```
2. Rebuild GRUB2
   ```
   sudo grub-mkstandalone -o /boot.efi -d /usr/lib/grub/x86_64-efi -O x86_64-efi --compress=xz /boot/grub/grub.cfg
   ```
3. Upload `boot.efi` to some place accessible by macOS.
4. Reboot into macOS.
5. Mount "Ubuntu Boot Loader" and replace the old `boot.efi` file in
   that partition with the new `boot.efi` file. Remember that it must
   be done with the Terminal as Finder glitches out.
6. I doubt this must be done, but you may need to re-bless the partition.

## Acknowledgments

* Nailen Matschke (nailen@caltech.edu) for instructions on how to boot
  into Ubuntu from Apple's native bootloader via intermediately
  booting into a standalone GRUB2 bootloader.
* github.com/chisNaN for easy instructions to install and configure
  the keyboard and touchpad drivers.
