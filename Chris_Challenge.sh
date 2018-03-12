#!/bin/sh
	sqlcmd.sh -bC "SELECT substr(int_to_serial(rs.network_id),1,10),
	substr(int_to_serial(routed_id),1,10), nd.routing_depth 
	FROM routing_set rs 
	JOIN network_device nd
	ON rs.network_id=nd.network_id
	-- where ND.NETWORK_ID in 
	-- (select routed_id from routing_set where network_id = serial_to_int('001F4C57B0') and action is null)
	ORDER BY 2,3 desc nulls last,1;" > result
	while read -r line; do
		line=`echo $line | sed -r 's/^ *//;s/[[:space:]]*//g'`
		parent=`echo $line | cut -d, -f 1`	# meter serial
		prevChild=$child
		child=`echo $line | cut -d, -f 2`
		depth=`echo $line | cut -d, -f 3`
		if [[ $child = $prevChild ]]; then
			value="$value---$parent,$depth"
			continue
		else
			echo $value
			value="$child---$parent,$depth"
		fi
	done < $result > neatlyFormatted
	echo $value >> neatlyFormatted


