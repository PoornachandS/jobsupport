import boto3

ec2 = boto3.client('ec2')

if __name__ == "__main__":
    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-code', 
            'Values': [16]
        }
    ]
    
    # filter the instances based on filters() above
    instances = ec2.filter(Filters=filters)
	instances_response	= json.loads(instances)
	instances_list = instances_response.get('Instances')

	Headers = "InstanceId#AvailabilityZone" + "\n"
    for instance in instances_list:
		instanceid = instance['InstanceId']
		availabilityzone = instance.get('AvailabilityZone')
		RunningInstances = [instanceid, availabilityzone]
		new_line = "#".join(RunningInstances) + "\n"
		if new_line[-1] != "\n":
			new_line = new_line + "\n"
		
		Headers = Headers + new_line

	
		