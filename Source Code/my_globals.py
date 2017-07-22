class my_globals:
	# main
		# for size_reducer
	size_reducer	=	0
		# for downloading and uploading
	download_prsd	=	0
	upload_prsd		=	0
		# for restarting
	go_restart		=	0
	main_crop_im	=	None
		# resizing factor for width and height
	r_factor		=	1
		# screen width and height
	sc_w			=	None
	sc_h			=	None
	input_dir		=	""
	output_dir		=	""
	width 			= 	1080
	height 			= 	1920
	input_file		=	""
	input_im		=	None
	all_i_files 	= 	[]
	all_o_files		=	[]
	cu_ind 			= 	0
	total_files		=	0
	last_start		=	0
	# crop_window
	im_c 			=	None
	im 				= 	None
	show_im 		= 	None
	f_im_c 			=	None
	w 				=	0
	h 				=	0
	mouse_x			=	w/2
	mouse_y			=	h/2
	skip			=	0
	# frame coords
	x1				=	0
	y1				=	0
	x2				=	0
	y2				=	0
	# qual_window
	out_format		=	"JPEG"
	Quality			=	80
	output_file		=	""
	crop_im 		=	None
	memory			=	0
	crop_im_canvas	=	None
	back 			=	0
	# io_window
	exit 			= 	0
	from_last		=	0
	cu_ind			=	0
	# download_window
	dwld_output_dir	=	""
	# s3_window
	dir_adrs		=	""
	level			=	0
	bucket_keys		=	[]
	# size reducer
	do_encode		=	1
	do_optimize		=	1
	do_c_crop		=	0
	min_m 			=	50
	max_m 	  		=	200
	min_q 	  		=	85
	bse_q 	  		=	90
	max_q 	  		=	95
	form	  		=	"JPEG"