import process

def create_partition(device, logger):
    timeout = 10
    cmd = "echo -e 'o\\nn\\np\\n1\\n\\n\\nw\\n' | fdisk %s" % device
    result = process.run(cmd, shell=True, ignore_status=True)
    if result.exit_status:
        logger.error("cmd failed: %s" % cmd)
        logger.error("out: %s" % result.stderr)
    while timeout > 0:
        if os.path.exists(device):
            cmd = "dd if=/dev/zero of=%s bs=512 count=10000; sync" % device
            result = process.run(cmd, shell=True, ignore_status=True)
            if result.exit_status:
                logger.error("cmd failed: %s" % cmd)
                logger.error("out: %s" % result.stderr)
            return True
        cmd = "partprobe %s" % device
        result = process.run(cmd, shell=True, ignore_status=True)
        if result.exit_status:
            logger.error("cmd failed: %s" % cmd)
            logger.error("out: %s" % result.stderr)
        time.sleep(1)
        timeout = timeout - 1
    return False