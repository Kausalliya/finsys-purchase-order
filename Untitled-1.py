
                        def add_inv_customer():
                            
                            inv_frame_1.grid_forget()
                            inv_frame_2 = Frame(tab3_3)
                            inv_frame_2.grid(row=0,column=0,sticky='nsew')

                            def inc_responsive_widgets2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("acpoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                                dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.45


                                dcanvas.coords("acpoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                                dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                                dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                                dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                                dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                                dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                                dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                                dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                                dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                                dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                                dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                                dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                                dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                                dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                                dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                                dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                                dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                                dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                                dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                                dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                                dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                                dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                                dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                                dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                                dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                                dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                                dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                                dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                                dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                                dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                                dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                                dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                                dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                                dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                                dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                                dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                                dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                                dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                                dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                                dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                                dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                                dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                                dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                                dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                                dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                                dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                                dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                                dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                                dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                                dcanvas.coords("acbutton2",dwidth/23,dheight/3.415)


                            inv_canvas_2=Canvas(inv_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                            inv_frame_2.grid_columnconfigure(0,weight=1)
                            inv_frame_2.grid_rowconfigure(0,weight=1)

                            
                            vertibar=Scrollbar(inv_frame_2, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=inv_canvas_2.yview)

                            inv_canvas_2.bind("<Configure>", inc_responsive_widgets2)
                            inv_canvas_2.config(yscrollcommand=vertibar.set)
                            inv_canvas_2.grid(row=0,column=0,sticky='nsew')

                            def sales_add_inv_cus():
                                title = ic_comb_cus_1.get()
                                firstname = ic_entry_cus_1.get()
                                lastname = ic_entry_cus_2.get()
                                company = ic_entry_cus_3.get()
                                location = ic_cus_4.get()
                                gsttype = ic_comb_cus_2.get()
                                gstin = ic_entry_cus_5.get()
                                panno = ic_entry_cus_6.get()
                                email = ic_entry_cus_7.get()
                                website = ic_entry_cus_8.get()
                                mobile = ic_entry_cus_9.get()
                                street = ic_entry_cus_10.get()
                                city = ic_entry_cus_12.get()
                                state = ic_entry_cus_13.get()
                                pincode = ic_entry_cus_p12.get()
                                country = ic_entry_cus_c13.get()
                                shipstreet = ic_entry_cus_11.get()
                                shipcity = ic_entry_cus_14.get()
                                shipstate = ic_entry_cus_15.get()
                                shippincode = ic_entry_cus_p14.get()
                                shipcountry = ic_entry_cus_c15.get()

                                usri_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usri_val = (nm_ent.get(),)
                                fbcursor.execute(usri_sql,usri_val)
                                usri_data = fbcursor.fetchone()

                                cmpi_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpi_val = (usri_data[0],)
                                fbcursor.execute(cmpi_sql,cmpi_val)
                                cmpi_data = fbcursor.fetchone()
                                cid = cmpi_data[0]

                                if ic_chk_str_1.get() == True:

                                    cus_sql = "INSERT INTO app1_customer (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                    cus_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid)
                                    fbcursor.execute(cus_sql,cus_val)
                                    finsysdb.commit()

                                    #----------Refresh Insert Tree--------#

                                    for record in cus_tree.get_children():
                                            cus_tree.delete(record)

                                    sql_pr="select * from auth_user where username=%s"
                                    sql_pr_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_pr,sql_pr_val,)
                                    pr_dtl=fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (pr_dtl[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dtl=fbcursor.fetchone()

                                    c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                                    c_val_1 = (cmp_dtl[0],)
                                    fbcursor.execute(c_sql_1,c_val_1,)
                                    c_data_1 = fbcursor.fetchall()

                                    count0 = 0
                                    for i in c_data_1:
                                        if True:
                                            cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                        else:
                                            pass
                                    count0 += 1

                                    inv_frame_2.destroy()
                                    inv_frame_1.grid(row=0,column=0,sticky='nsew')
                                
                                else:
                                    pass
                            

                            inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                            label_1 = Label(inv_canvas_2,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                            inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                            inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

                            label_1 = Label(inv_canvas_2,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

                            inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

                            label_2 = Label(inv_canvas_2,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

                            ic_comb_cus_1 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
                            ic_comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
                            ic_comb_cus_1.current(0)
                            window_ic_comb_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_1, tags=("accombo1"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

                            ic_entry_cus_1=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_1, tags=("acentry1"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

                            ic_entry_cus_2=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_2, tags=("acentry2"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

                            ic_entry_cus_3=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_3 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_3, tags=("acentry3"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

                            ic_cus_4=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_cus_4 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_cus_4, tags=("acentry4"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

                            ic_comb_cus_2 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
                            ic_comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
                            ic_comb_cus_2.current(0)
                            window_ic_comb_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_2, tags=("accombo2"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

                            def igst_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                ic_entry_cus_5.config(fg="white")
                                return True

                            def igst_invalidate():
                                ic_entry_cus_5.config(fg="red")


                            def ic_gst_in(event):
                                if ic_entry_cus_5.get()=="29APPCK7465F1Z1":
                                    ic_entry_cus_5.delete(0,END)
                                else:
                                    pass
                            
                            ic_entry_cus_5=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                            ival_gst = (inv_canvas_2.register(igst_validate), '%P')
                            iival_gst = (inv_canvas_2.register(igst_invalidate),)
                            ic_entry_cus_5.config(validate='focusout', validatecommand=ival_gst, invalidcommand=iival_gst)
                            window_ic_entry_cus_5 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_5, tags=("acentry5"))
                            ic_entry_cus_5.insert(0,"29APPCK7465F1Z1")
                            ic_entry_cus_5.bind("<Button-1>",ic_gst_in)

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

                            def ic_pan_no(event):
                                if ic_entry_cus_6.get()=="APPCK7465F":
                                    ic_entry_cus_6.delete(0,END)
                                else:
                                    pass

                            def ipan_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z]{5}\d{4}[A-Za-z]{1}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                ic_entry_cus_6.config(fg="white")
                                return True

                            def ipan_invalidate():
                                ic_entry_cus_6.config(fg="red")

                            ic_entry_cus_6=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                            ival_pan = (inv_canvas_2.register(ipan_validate), '%P')
                            iival_pan = (inv_canvas_2.register(ipan_invalidate),)
                            ic_entry_cus_6.config(validate='focusout', validatecommand=ival_pan, invalidcommand=iival_pan)
                            window_ic_entry_cus_6 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_6, tags=("acentry6"))
                            ic_entry_cus_6.insert(0,"APPCK7465F")
                            ic_entry_cus_6.bind("<Button-1>",ic_pan_no)

                            label_2 = Label(inv_canvas_2,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

                            def iemail_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                ic_entry_cus_7.config(fg="white")
                                return True

                            def iemail_invalidate():
                                ic_entry_cus_7.config(fg="red")

                            ic_entry_cus_7=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f')
                            ival_email = (inv_canvas_2.register(iemail_validate), '%P')
                            iival_email = (inv_canvas_2.register(iemail_invalidate),)
                            ic_entry_cus_7.config(validate='focusout', validatecommand=ival_email, invalidcommand=iival_email)
                            window_ic_entry_cus_7 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_7, tags=("acentry7"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

                            ic_entry_cus_8=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_8 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_8, tags=("acentry8"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

                            def imobile_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[0-9]{10}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                ic_entry_cus_9.config(fg="white")
                                return True

                            def imobile_invalidate():
                                ic_entry_cus_9.config(fg="red")

                            ic_entry_cus_9=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            ival_mobile = (inv_canvas_2.register(imobile_validate), '%P')
                            iival_mobile = (inv_canvas_2.register(imobile_invalidate),)
                            ic_entry_cus_9.config(validate='focusout', validatecommand=ival_mobile, invalidcommand=iival_mobile)
                            window_ic_entry_cus_9 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_9, tags=("acentry9"))

                            def copy_icus_details():
                                ic_entry_cus_11.delete(0, END)
                                ic_entry_cus_11.insert(0,ic_entry_cus_10.get())
                                ic_entry_cus_14.delete(0, END)
                                ic_entry_cus_14.insert(0,ic_entry_cus_12.get())
                                ic_entry_cus_15.delete(0, END)
                                ic_entry_cus_15.insert(0,ic_entry_cus_13.get())
                                ic_entry_cus_p14.delete(0, END)
                                ic_entry_cus_p14.insert(0,ic_entry_cus_p12.get())
                                ic_entry_cus_c15.delete(0, END)
                                ic_entry_cus_c15.insert(0,ic_entry_cus_c13.get())

                            label_1 = Label(inv_canvas_2,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
                            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

                            label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

                            ic_entry_cus_10=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_10 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_10, tags=("acentry10"))

                            label_1 = Label(inv_canvas_2,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
                            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

                            ic_chk_str = StringVar()
                            ic_chkbtn1 = Checkbutton(inv_canvas_2, text = "Same As Billing Address", variable = ic_chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f",command=copy_icus_details)
                            ic_chkbtn1.select()
                            window_ic_chkbtn_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn1, tags=("accheck1"))

                            label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

                            ic_entry_cus_11=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_11 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_11, tags=("acentry11"))

                            label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

                            ic_entry_cus_12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_12, tags=("acentry12"))
                            
                            label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

                            ic_entry_cus_13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_13, tags=("acentry13"))

                            label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

                            ic_entry_cus_14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_14, tags=("acentry14"))

                            label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

                            ic_entry_cus_15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_15, tags=("acentry15"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

                            ic_entry_cus_p12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_p12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_p12, tags=("acentry16"))
                            
                            label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

                            ic_entry_cus_c13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_c13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_c13, tags=("acentry17"))

                            label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

                            ic_entry_cus_p14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_p14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_p14, tags=("acentry18"))

                            label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

                            ic_entry_cus_c15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ic_entry_cus_c15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_c15, tags=("acentry19"))

                            ic_chk_str_1 = BooleanVar()
                            ic_chkbtn2 = Checkbutton(inv_canvas_2, text = "Agree to terms and conditions", variable = ic_chk_str_1, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            window_ic_chkbtn_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn2,tags=("accheck2"))

                            ic_cus_btn2=Button(inv_canvas_2,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_inv_cus)
                            window_ic_cus_btn2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_cus_btn2,tags=("acbutton1"))

                            def inv_back_1_():
                                inv_frame_2.grid_forget()
                                inv_frame_1.grid(row=0,column=0,sticky='nsew')

                            bck_btn1=Button(inv_canvas_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
                            window_bck_btn1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('acbutton2'))
                            


                        aibtn2=Button(inv_canvas_1,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_inv_customer)
                        window_aibtn2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=aibtn2, tags=('aibutton1'))

                        label_2 = Label(inv_canvas_1,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel6'))

                        aientry_1=Entry(inv_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_aientry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30,window=aientry_1,tags=('aientry1'))


                        label_2 = Label(inv_canvas_1,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel8'))


                        label_2 = Label(inv_canvas_1,width=6,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel9'))


                        ai_b_entry_1=scrolledtext.ScrolledText(inv_canvas_1,width=30,background='#2f516f',foreground="white")
                        window_ai_b_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=150, window=ai_b_entry_1,tags=('aientry2'))

                        label_2 = Label(inv_canvas_1,width=12,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel10'))
                        

                        def select_format(event):
                            if ai_p_comb_2.get()=="Kerala":
                                print(ai_p_comb_2.get())
                                inv_canvas_1.itemconfig(window_label_cgst,state='normal')
                                inv_canvas_1.itemconfig(window_label_sgst,state='normal')
                                inv_canvas_1.itemconfig(window_cgst_entry,state='normal')
                                inv_canvas_1.itemconfig(window_sgst_entry,state='normal')
                                inv_canvas_1.itemconfig(window_label_igst,state='hidden')
                                inv_canvas_1.itemconfig( window_igst_entry,state='hidden')
                                inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
                            else:
                                print(ai_p_comb_2.get())
                                inv_canvas_1.itemconfig(window_label_cgst,state='hidden')
                                inv_canvas_1.itemconfig(window_label_sgst,state='hidden')
                                inv_canvas_1.itemconfig(window_label_igst,state='normal')
                                inv_canvas_1.itemconfig( window_igst_entry,state='normal')
                                inv_canvas_1.delete(p_line)
                                inv_canvas_1.itemconfig( window_cgst_entry,state='hidden')
                                inv_canvas_1.itemconfig( window_sgst_entry,state='hidden')

                              
                        ai_p_comb_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_p_comb_2['values'] = ("Choose...","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
                        ai_p_comb_2.current(0)
                        ai_p_comb_2.bind("<<ComboboxSelected>>",select_format)
                        window_ai_p_comb_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=ai_p_comb_2,tags=('aicombo3'))


                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine1'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine2'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine3'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine4'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine5'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine6'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine7'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine8'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine9'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine10'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine11'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine12'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine13'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine14'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine15'))


                        label_2 = Label(inv_canvas_1,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel11'))

                        label_3 = Label(inv_canvas_1,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_3 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_3,tags=('ailabel12'))

                        label_4 = Label(inv_canvas_1,width=4,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel13'))

                        label_4 = Label(inv_canvas_1,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel14'))

                        label_4 = Label(inv_canvas_1,width=4,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel15'))

                        label_4 = Label(inv_canvas_1,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel16'))

                        label_4 = Label(inv_canvas_1,width=6,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel17'))

                        label_4 = Label(inv_canvas_1,width=7,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel18'))


                        def i_details_1(event):
                            inv_to_str = ai_comb_p_1 .get()
                            sql = "select * from app1_item where name=%s and cid_id=%s"
                            val = (inv_to_str,cmp_dtl[0],)
                            fbcursor.execute(sql,val)
                            inv_c_sel = fbcursor.fetchone()
                            ai_entry_p_1.delete(0,END)
                            ai_entry_p_1.insert(0,inv_c_sel[4])
                            ai_entry_p_1_2.delete('1.0',END)
                            ai_entry_p_1_2.insert('1.0',inv_c_sel[12])
                            ai_entry_p_1_4.delete(0,END)
                            ai_entry_p_1_4.insert(0,inv_c_sel[7])
                            p_ava1['text']="Avilable Qty:"+inv_c_sel[18] 

                        sql_pr="select * from auth_user where username=%s"
                        sql_pr_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pr,sql_pr_val,)
                        pr_dtl=fbcursor.fetchone()

                        sql = "select * from app1_company where id_id=%s"
                        val = (pr_dtl[0],)
                        fbcursor.execute(sql, val,)
                        cmp_dtl=fbcursor.fetchone()
                                    

                        sql_pr_cmp="select name from app1_item where cid_id=%s"
                        sql_pr_cmp_val=(cmp_dtl[0],)
                        fbcursor.execute(sql_pr_cmp,sql_pr_cmp_val,)
                        pr_cmp_dtl=fbcursor.fetchall()
                        pi_i1 = []

                        for i in pr_cmp_dtl:
                            pi_i1.append(str(i[0]))   

                        label_2 = Label(inv_canvas_1,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(90, 1020, anchor="nw", window=label_2,tags=('ailabel19'))

                        ai_comb_p_1 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_p_1 ['values'] = pi_i1
                        window_ai_comb_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_1,tags=('aicombo4'))
                        ai_comb_p_1.bind("<<ComboboxSelected>>",i_details_1)
                        
                        def add_item():
                            inv_frame_1.grid_forget()
                            item_frame_1 = Frame(tab3_3)
                            item_frame_1.grid(row=0,column=0,sticky='nsew')

                            def item_responsive_widgets_1(event):

                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                                
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("ittpoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("ittlabel1",dwidth/2.3,dheight/8.24)
                                dcanvas.coords("itthline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.35


                                dcanvas.coords("ittpoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("ittbutton1",dwidth/23,dheight/3.415)

                                dcanvas.coords("ittlabel2",dwidth/13.85,dheight/1.82)
                                dcanvas.coords("ittlabel3",dwidth/1.935,dheight/1.82)
                                dcanvas.coords("ittlabel4",dwidth/13.85,dheight/1.39)
                                dcanvas.coords("ittlabel5",dwidth/1.93,dheight/1.39)
                                dcanvas.coords("ittlabel6",dwidth/13.85,dheight/0.95)
                                dcanvas.coords("ittlabel7",dwidth/13.85,dheight/1.09)
                                dcanvas.coords("ittcheck1",dwidth/4,dheight/1.09)
                                dcanvas.coords("ittcheck2",dwidth/2.5,dheight/1.09)
                                dcanvas.coords("ittlabel8",dwidth/1.935,dheight/0.95)
                                dcanvas.coords("ittlabel9",dwidth/13.85,dheight/0.79)
                                dcanvas.coords("ittlabel10",dwidth/1.935,dheight/0.79)
                                dcanvas.coords("ittlabel11",dwidth/13.85,dheight/0.67)
                                dcanvas.coords("ittlabel12",dwidth/1.935,dheight/0.67)
                                dcanvas.coords("ittlabel13",dwidth/13.85,dheight/0.568)
                                dcanvas.coords("ittlabel14",dwidth/13.85,dheight/0.5)
                                dcanvas.coords("ittlabel15",dwidth/1.935,dheight/0.5)
                                dcanvas.coords("ittcheck3",dwidth/13.85,dheight/0.45)
                                dcanvas.coords("ittlabel16",dwidth/13.85,dheight/0.43)
                                dcanvas.coords("ittlabel17",dwidth/1.935,dheight/0.43)
                                dcanvas.coords("ittlabel18",dwidth/13.85,dheight/0.39)
                                dcanvas.coords("ittcheck4",dwidth/4,dheight/0.39)
                                dcanvas.coords("ittcheck5",dwidth/2.5,dheight/0.39)

                                dcanvas.coords("ittentry1",dwidth/1.93,dheight/1.66)
                                dcanvas.coords("ittentry2",dwidth/13.8,dheight/1.3)
                                dcanvas.coords("ittentry3",dwidth/1.93,dheight/1.3)
                                dcanvas.coords("ittentry4",dwidth/13.8,dheight/0.9)
                                dcanvas.coords("ittentry5",dwidth/8.6,dheight/0.9)
                                dcanvas.coords("ittentry6",dwidth/1.92,dheight/0.9)
                                dcanvas.coords("ittentry7",dwidth/1.77,dheight/0.9)
                                dcanvas.coords("ittentry8",dwidth/13.8,dheight/0.76)
                                dcanvas.coords("ittentry9",dwidth/1.93,dheight/0.76)
                                dcanvas.coords("ittentry10",dwidth/13.8,dheight/0.65)
                                dcanvas.coords("ittentry11",dwidth/1.93,dheight/0.65)
                                dcanvas.coords("ittentry12",dwidth/13.8,dheight/0.55)
                                dcanvas.coords("ittentry13",dwidth/13.8,dheight/0.488)
                                dcanvas.coords("ittentry14",dwidth/1.93,dheight/0.488)
                                dcanvas.coords("ittentry15",dwidth/13.8,dheight/0.42)
                                dcanvas.coords("ittentry16",dwidth/1.93,dheight/0.42)

                                dcanvas.coords("ittbutton2",dwidth/2.2,dheight/0.375)
                                
                                dcanvas.coords("ittdentry1",dwidth/13.8,dheight/1.66)

                                dcanvas.coords("ittbutton3",dwidth/2.3,dheight/1.3)

                                dcanvas.coords("itllabel1",dwidth/1.93,dheight/1.2)
                                
                            item_canvas_1=Canvas(item_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

                            item_frame_1.grid_columnconfigure(0,weight=1)
                            item_frame_1.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(item_frame_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=item_canvas_1.yview)

                            item_canvas_1.bind("<Configure>", item_responsive_widgets_1)
                            item_canvas_1.config(yscrollcommand=vertibar.set)
                            item_canvas_1.grid(row=0,column=0,sticky='nsew')

                            def insert_item():
                                
                                name = itt_entry_1.get()
                                type = itt_comb_1.get()
                                unit = itt_entry_2.get()
                                hsncode = itt_entry_3.get()
                                taxable = itt_chk_str_1.get()
                                nontaxable = itt_chk_str_2.get()
                                purchaseprice = itt_entry_4.get()
                                purchaseaccount = itt_comb_2.get()
                                purchasedes = ittsctext1.get(1.0,END)
                                salesprice = itt_entry_5.get()
                                salesaccount = itt_comb_3.get()
                                salesdes = ittsctext2.get(1.0,END)
                                taxrate = itt_comb_4.get()
                                intrastatetaxrate = itt_comb_5.get()
                                interstatetaxrate = itt_comb_6.get()
                                trackinventory = itt_chk_str_3.get()
                                inventoryaccount = itt_comb_7.get()
                                stockonhand = itt_spin_1.get()
                                active = itt_chk_str_4.get()
                                inactive = itt_chk_str_5.get()

                                usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp_val = (nm_ent.get(),)
                                fbcursor.execute(usrp_sql,usrp_val)
                                usrp_data = fbcursor.fetchone()

                                cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp_val = (usrp_data[0],)
                                fbcursor.execute(cmpp_sql,cmpp_val)
                                cmpp_data = fbcursor.fetchone()
                                cid = cmpp_data[0]

                                it_sql = "INSERT INTO app1_item(name,type,unit,hsncode,taxable,nontaxable,purchaseprice,purchaseaccount,purchasedes,salesprice,salesaccount,salesdes,taxrate,intrastatetaxrate,interstatetaxrate,trackinventory,inventoryaccount,stockonhand,active,inactive,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                it_val = (name,type,unit,hsncode,taxable,nontaxable,purchaseprice,purchaseaccount,purchasedes,salesprice,salesaccount,salesdes,taxrate,intrastatetaxrate,interstatetaxrate,trackinventory,inventoryaccount,stockonhand,active,inactive,cid)
                                fbcursor.execute(it_sql,it_val)
                                finsysdb.commit()

                                item_frame_1.grid_forget()
                                inv_frame_1.grid(row=0,column=0,sticky='nsew')
                                    

                            item_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ittpoly1"))

                            label_1 = Label(item_canvas_1,width=23,height=1,text="ADD ITEM", font=('arial 20'),background="#1b3857",fg="white",anchor="w") 
                            window_label_1 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ittlabel1"))

                            item_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("itthline"))

                            item_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ittpoly2"))

                            label_1 = Label(item_canvas_1,width=13,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white", anchor="w") 
                            window_label_1 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ittlabel2'))

                            itt_entry_1=Entry(item_canvas_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_itt_entry_1 = item_canvas_1.create_window(0, 0, anchor="nw", height=30,window=itt_entry_1, tags=('ittdentry1'))
                            
                            label_1 = Label(item_canvas_1,width=13,height=1,text="Type", font=('arial 12'),background="#1b3857",fg="white", anchor="w") 
                            window_label_1 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ittlabel3'))
    

                            itt_comb_1 = ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_comb_1['values'] = ("Choose...","Goods","Services")
                            itt_comb_1.current(0)
                            window_itt_comb_1 = item_canvas_1.create_window(0, 0, anchor="nw", width=535,height=30,window=itt_comb_1,tags=('ittentry1'))
                            

                            label_1 = Label(item_canvas_1,width=10,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_1 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ittlabel4'))

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()


                            sql = "select unitsymbol,unitname from app1_unit where cid_id=%s"
                            val = (cdtl[0],)
                            fbcursor.execute(sql,val,)
                            uni_in_ac_data = fbcursor.fetchall()
                            uc_data_1 = ["Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",]
                            for i in uni_in_ac_data:
                                uc_data_1.insert(-1,str(i[0])+" "+str(i[1]))
                                

                            itt_entry_2=ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_entry_2['values'] = (uc_data_1)
                            itt_entry_2.current(0)
                            window_itt_entry_2 = item_canvas_1.create_window(0, 0, anchor="nw", width=482, height=30,window=itt_entry_2, tags=('ittentry2'))

                            def unit_create():
                                item_frame_1.grid_forget()
                                item_frame_2 = Frame(tab3_3)
                                item_frame_2.grid(row=0,column=0,sticky='nsew')

                                def item_responsive_widgets_2(event):

                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                    
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("uittpoly1",x1 + r1,y1,
                                    x1 + r1,y1,
                                    x2 - r1,y1,
                                    x2 - r1,y1,     
                                    x2,y1,     
                                    #--------------------
                                    x2,y1 + r1,     
                                    x2,y1 + r1,     
                                    x2,y2 - r1,     
                                    x2,y2 - r1,     
                                    x2,y2,
                                    #--------------------
                                    x2 - r1,y2,     
                                    x2 - r1,y2,     
                                    x1 + r1,y2,
                                    x1 + r1,y2,
                                    x1,y2,
                                    #--------------------
                                    x1,y2 - r1,
                                    x1,y2 - r1,
                                    x1,y1 + r1,
                                    x1,y1 + r1,
                                    x1,y1,
                                    )

                                    dcanvas.coords("uittlabel1",dwidth/2.3,dheight/8.24)
                                    dcanvas.coords("uitthline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/1.1


                                    dcanvas.coords("uittpoly2",x11 + r2,y11,
                                    x11 + r2,y11,
                                    x21 - r2,y11,
                                    x21 - r2,y11,     
                                    x21,y11,     
                                    #--------------------
                                    x21,y11 + r2,     
                                    x21,y11 + r2,     
                                    x21,y21 - r2,     
                                    x21,y21 - r2,     
                                    x21,y21,
                                    #--------------------
                                    x21 - r2,y21,     
                                    x21 - r2,y21,     
                                    x11 + r2,y21,
                                    x11 + r2,y21,
                                    x11,y21,
                                    #--------------------
                                    x11,y21 - r2,
                                    x11,y21 - r2,
                                    x11,y11 + r2,
                                    x11,y11 + r2,
                                    x11,y11,
                                    )

                                    dcanvas.coords("uittbutton1",dwidth/23,dheight/3.415)

                                    dcanvas.coords("uittlabel2",dwidth/13.85,dheight/1.82)
                                    dcanvas.coords("uittlabel3",dwidth/1.935,dheight/1.82)

                                    dcanvas.coords("uittentry1",dwidth/13.85,dheight/1.66)
                                    dcanvas.coords("uittentry2",dwidth/1.93,dheight/1.66)

                                    dcanvas.coords("uittbutton2",dwidth/2.2,dheight/1.3)

                                item_canvas_2=Canvas(item_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

                                item_frame_2.grid_columnconfigure(0,weight=1)
                                item_frame_2.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(item_frame_2, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=item_canvas_2.yview)

                                item_canvas_2.bind("<Configure>", item_responsive_widgets_2)
                                item_canvas_2.config(yscrollcommand=vertibar.set)
                                item_canvas_2.grid(row=0,column=0,sticky='nsew')

                                def insert_unit():

                                    unitsymbol = uitt_entry_1.get()
                                    unitname = uitt_entry_2.get()

                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    uc_sql = "INSERT INTO app1_unit(unitsymbol,unitname,cid_id) VALUES(%s,%s,%s)"
                                    uc_val = (unitsymbol,unitname,cid)
                                    fbcursor.execute(uc_sql,uc_val)
                                    finsysdb.commit()
                                    
                                    item_frame_2.destroy()
                                    item_frame_1.grid(row=0,column=0,sticky='nsew')
                                        

                                item_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("uittpoly1"))

                                label_1 = Label(item_canvas_2,width=23,height=1,text="UNIT CREATE", font=('arial 20'),background="#1b3857",fg="white",anchor="w") 
                                window_label_1 = item_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("uittlabel1"))

                                item_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("uitthline"))

                                item_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("uittpoly2"))

                                label_1 = Label(item_canvas_2,width=13,height=1,text="Unit Symbol", font=('arial 12'),background="#1b3857",fg="white", anchor="w") 
                                window_label_1 = item_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('uittlabel2'))

                                uitt_entry_1=Entry(item_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_uitt_entry_1 = item_canvas_2.create_window(0, 0, anchor="nw", height=30,window=uitt_entry_1, tags=('uittentry1'))
                                
                                label_1 = Label(item_canvas_2,width=13,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white", anchor="w") 
                                window_label_1 = item_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('uittlabel3'))

                                uitt_entry_2=Entry(item_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_uitt_entry_2 = item_canvas_2.create_window(0, 0, anchor="nw", height=30,window=uitt_entry_2, tags=('uittentry2'))

                                uitt_save_btn1=Button(item_canvas_2,text='Create', width=15,height=2,foreground="white",background="#1b3857",font='arial 12',command=insert_unit)
                                window_uitt_save_btn1 = item_canvas_2.create_window(0, 0, anchor="nw", window=uitt_save_btn1,tags=('uittbutton2'))

                                def uitem_back_1_():
                                    item_frame_2.grid_forget()
                                    item_frame_1.grid(row=0,column=0,sticky='nsew')

                                uitt_bck_btn1=Button(item_canvas_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=uitem_back_1_)
                                window_uitt_bck_btn1 = item_canvas_2.create_window(0, 0, anchor="nw", window=uitt_bck_btn1,tags=('uittbutton1'))
        

                            itbtn1=Button(item_canvas_1,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=unit_create)
                            window_itbtn1 = item_canvas_1.create_window(0, 0, anchor="nw", window=itbtn1, tags=('ittbutton3'))

                            label_1 = Label(item_canvas_1,width=10,height=1,text="HSN code", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_1 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ittlabel5'))

                            def hsn_validate_1(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[0-9]{8}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                itt_entry_3.config(fg="white")
                                return True

                            def on_hsn_validate_1():
                                itt_entry_3.config(fg="red")

                            itt_entry_3=Entry(item_canvas_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            hsnvl = (item_canvas_1.register(hsn_validate_1), '%P')
                            hsnivl = (item_canvas_1.register(on_hsn_validate_1),)
                            itt_entry_3.config(validate='focusout', validatecommand=hsnvl, invalidcommand=hsnivl)
                            window_itt_entry_3 = item_canvas_1.create_window(0, 0, anchor="nw", height=30,window=itt_entry_3, tags=('ittentry3'))

                            #Define a callback function
                            def callback(url):
                                webbrowser.open_new_tab(url)

                            link_1 = Label(item_canvas_1,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                            window_link_1 = item_canvas_1.create_window(0, 0, anchor="nw", window=link_1, tags=('itllabel1'))
                            link_1.bind("<Button-1>", lambda e:
                            callback("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))



                            label_2 = Label(item_canvas_1,width=20,height=1,text="Tax Reference", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel7"))


                            itt_chk_str_1 = BooleanVar()
                            itt_chkbtn1 = Checkbutton(item_canvas_1, text = "Taxable", variable = itt_chk_str_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            # itt_chkbtn1.select()
                            window_itt_chkbtn_1 = item_canvas_1.create_window(0, 0, anchor="nw", window=itt_chkbtn1, tags=("ittcheck1"))

                            itt_chk_str_2 = BooleanVar()
                            itt_chkbtn2 = Checkbutton(item_canvas_1, text = "Non Taxable", variable = itt_chk_str_2, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            # itt_chkbtn2.select()
                            window_itt_chkbtn_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=itt_chkbtn2, tags=("ittcheck2"))


                            label_2 = Label(item_canvas_1,width=20,height=1,text="Purchase Price", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel6"))

                            itbtn2=Button(item_canvas_1,text='INR', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
                            window_itbtn2 = item_canvas_1.create_window(0, 0, anchor="nw", window=itbtn2, tags=('ittentry4'))

                            itt_entry_4=Entry(item_canvas_1,width=79,justify=LEFT,background='#2f516f',foreground="white")
                            window_itt_entry_4 = item_canvas_1.create_window(0, 0, anchor="nw", height=30,window=itt_entry_4, tags=('ittentry5'))

                            label_2 = Label(item_canvas_1,width=20,height=1,text="Account", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel9"))

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            c_sql_i1 = "SELECT name FROM app1_accounts1 where acctype=%s and cid_id=%s"
                            c_val_i1 = ('Cost of Goods Sold',inv_dtls[0],)
                            fbcursor.execute(c_sql_i1,c_val_i1,)
                            pa_data_5 = fbcursor.fetchall()
                            pa_data_1 = []

                            for i in pa_data_5:
                                pa_data_1.insert(-1,i[0])


                            itt_comb_2 = ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_comb_2['values'] = (pa_data_1)
                            window_itt_comb_2 = item_canvas_1.create_window(0, 0, anchor="nw", width=535,height=30,window=itt_comb_2,tags=('ittentry8'))

                            label_2 = Label(item_canvas_1,width=20,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel11"))

                            ittsctext1=scrolledtext.ScrolledText(item_canvas_1,width=65,background='#2f516f',foreground="white")
                            window_ittsctext1 = item_canvas_1.create_window(0, 0, anchor="nw", height=60,window=ittsctext1,tags=('ittentry10'))

                            label_2 = Label(item_canvas_1,width=20,height=1,text="Sales Price", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel8"))

                            itbtn3=Button(item_canvas_1,text='INR', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
                            window_itbtn3 = item_canvas_1.create_window(0, 0, anchor="nw", window=itbtn3, tags=('ittentry6'))

                            itt_entry_5=Entry(item_canvas_1,width=79,justify=LEFT,background='#2f516f',foreground="white")
                            window_itt_entry_5 = item_canvas_1.create_window(0, 0, anchor="nw", height=30,window=itt_entry_5, tags=('ittentry7'))    

                            label_2 = Label(item_canvas_1,width=20,height=1,text="Account", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel10"))

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            c_sql_i1 = "SELECT name FROM app1_accounts1 where acctype=%s and cid_id=%s"
                            c_val_i1 = ('Income',inv_dtls[0],)
                            fbcursor.execute(c_sql_i1,c_val_i1,)
                            sa_data_5 = fbcursor.fetchall()
                            sa_data_1 = []

                            for i in sa_data_5:
                                sa_data_1.insert(-1,i[0])

                            itt_comb_3 = ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_comb_3['values'] = (sa_data_1)
                            window_itt_comb_3 = item_canvas_1.create_window(0, 0, anchor="nw", width=535,height=30,window=itt_comb_3,tags=('ittentry9'))

                            label_2 = Label(item_canvas_1,width=20,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel12"))

                            ittsctext2=scrolledtext.ScrolledText(item_canvas_1,width=65,background='#2f516f',foreground="white")
                            window_ittsctext2 = item_canvas_1.create_window(0, 0, anchor="nw", height=60,window=ittsctext2,tags=('ittentry11'))

                            label_2 = Label(item_canvas_1,width=20,height=1,text="Tax Rate", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel13"))

                            itt_comb_4 = ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_comb_4['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            itt_comb_4.current(0)
                            window_itt_comb_4 = item_canvas_1.create_window(0, 0, anchor="nw", width=535,height=30,window=itt_comb_4,tags=('ittentry12'))

                            label_2 = Label(item_canvas_1,width=25,height=1,text="Intra State Tax Rate", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel14"))

                            itt_comb_5 = ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_comb_5['values'] = ("Choose...","GST 0(0%)","GST 5(5%)","GST 12(12%)","GST 18(18%)","GST 28(28%)","Out of Scope(0%)",)
                            itt_comb_5.current(0)
                            window_itt_comb_5 = item_canvas_1.create_window(0, 0, anchor="nw", width=535,height=30,window=itt_comb_5,tags=('ittentry13'))

                            
                            label_2 = Label(item_canvas_1,width=25,height=1,text="Inter State Tax Rate", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel15"))

                            
                            itt_comb_6 = ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_comb_6['values'] = ("Choose...","IGST 0(0%)","IGST 5(5%)","IGST 12(12%)","IGST 18(18%)","IGST 28(28%)","Out of Scope(0%)",)
                            itt_comb_6.current(0)
                            window_itt_comb_6 = item_canvas_1.create_window(0, 0, anchor="nw", width=535,height=30,window=itt_comb_6,tags=('ittentry14'))

                            def track_inventory():
                                if itt_chk_str_3.get() == True:
                                    item_canvas_1.itemconfig('ittlabel16',state='normal')
                                    item_canvas_1.itemconfig('ittentry15',state='normal')
                                    item_canvas_1.itemconfig('ittlabel17',state='normal')
                                    item_canvas_1.itemconfig('ittentry16',state='normal')
                                else:
                                    item_canvas_1.itemconfig('ittlabel16',state='hidden')
                                    item_canvas_1.itemconfig('ittentry15',state='hidden')
                                    item_canvas_1.itemconfig('ittlabel17',state='hidden')
                                    item_canvas_1.itemconfig('ittentry16',state='hidden')

                            itt_chk_str_3 = BooleanVar()
                            itt_chkbtn3 = Checkbutton(item_canvas_1, text = "Track Inventory", variable = itt_chk_str_3, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=track_inventory)
                            # itt_chkbtn2.select()
                            window_itt_chkbtn_3 = item_canvas_1.create_window(0, 0, anchor="nw", window=itt_chkbtn3, tags=("ittcheck3"))


                            label_2 = Label(item_canvas_1,width=25,height=1,text="Inventory Account", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel16"),state=HIDDEN)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            c_sql_i1 = "SELECT name FROM app1_accounts1 where acctype=%s and cid_id=%s"
                            c_val_i1 = ('Current Assets',inv_dtls[0],)
                            fbcursor.execute(c_sql_i1,c_val_i1,)
                            ia_data_5 = fbcursor.fetchall()

                            ia_data_1 = []

                            for i in ia_data_5:
                                ia_data_1.insert(-1,i[0])

                            itt_comb_7 = ttk.Combobox(item_canvas_1,font=('arial 10'))
                            itt_comb_7['values'] = (ia_data_1)
                            window_itt_comb_7 = item_canvas_1.create_window(0, 0, anchor="nw", width=535,height=30,window=itt_comb_7,tags=('ittentry15'),state=HIDDEN)

                            label_2 = Label(item_canvas_1,width=25,height=1,text="Stock on Hand", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel17"),state=HIDDEN)

                            itt_spin_1=Spinbox(item_canvas_1,width=82,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_itt_spin_1 = item_canvas_1.create_window(0, 0, anchor="nw", height=30, window=itt_spin_1,tags=('ittentry16'),state=HIDDEN)

                            label_2 = Label(item_canvas_1,width=20,height=1,text="Active/Inactive", font=('arial 12'),background="#1b3857",fg="white",anchor="w") 
                            window_label_2 = item_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ittlabel18"))

                            
                            itt_chk_str_4 = StringVar()
                            
                            itt_chkbtn4 = ttk.Radiobutton(
                                item_canvas_1,
                                text="Active",
                                value="Active",
                                variable=itt_chk_str_4
                
                            )
                            window_itt_chkbtn_4 = item_canvas_1.create_window(0, 0, anchor="nw", window=itt_chkbtn4, tags=("ittcheck4"))

                            itt_chk_str_5 = StringVar()
                            
                            itt_chkbtn5 = ttk.Radiobutton(
                                item_canvas_1,
                                text="Inactive",
                                value="Inactive",
                                variable=itt_chk_str_5
                            )
                            window_itt_chkbtn_5 = item_canvas_1.create_window(0, 0, anchor="nw", window=itt_chkbtn5, tags=("ittcheck5"))

                            

                            itt_save_btn1=Button(item_canvas_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12',command=insert_item)
                            window_itt_save_btn1 = item_canvas_1.create_window(0, 0, anchor="nw", window=itt_save_btn1,tags=('ittbutton2'))

                            def item_back_1_():
                                item_frame_1.grid_forget()
                                inv_frame_1.grid(row=0,column=0,sticky='nsew')

                            itt_bck_btn1=Button(item_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=item_back_1_)
                            window_itt_bck_btn1 = item_canvas_1.create_window(0, 0, anchor="nw", window=itt_bck_btn1,tags=('ittbutton1'))
                        
                        taddbtn1=Button(inv_canvas_1,text='+', width=3,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_item)
                        window_tddbtn9 = inv_canvas_1.create_window(0, 0, anchor="nw", window=taddbtn1, tags=('puorderbutton9'))


                        ai_entry_p_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_ai_entry_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1,tags=('aientry3'))

                        ai_entry_p_1_2=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                        window_ai_entry_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_2,tags=('aientry4'))


                        ai_entry_p_1_4=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_p_1_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_4,tags=('aientry6'))

                        def multiply_num_i1(event):
                            num1= float(ai_entry_p_1_3.get())
                            num2= float(ai_entry_p_1_4.get())
                            mul_i= round(num1 * num2,2)
                            ai_entry_p_1_5.delete(0, END)
                            ai_entry_p_1_5.insert(0,mul_i)

                            
                            try:
                                n1 = float(en_str_1.get())
                            except:
                                n1=0.0
                            try:
                                n2 = float(en_str_2.get())
                            except:
                                n2 = 0.0
                            try:
                                n3 = float(en_str_3.get())
                            except:
                                n3 = 0.0
                            try:
                                n4 = float(en_str_4.get())
                            except:
                                n4 = 0.0
                            
                            sum_i = n1+n2+n3+n4
                            sub_entry_1.delete(0, END)
                            sub_entry_1.insert(0,round(sum_i,2))
                            if ai_p_comb_2.get()=="Kerala":
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                            else:
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))

                                                      
                        ai_entry_p_1_3=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_p_1_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_3,tags=('aientry5'))
                        ai_entry_p_1_3.bind("<Button-1>",multiply_num_i1)
                            
                        en_str_1 = StringVar()
                        ai_entry_p_1_5=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white",textvariable=en_str_1)
                        window_ai_entry_p_1_5 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_5,tags=('aientry7'))
                        
                        def tax_cal1(event):
                            global tax_amount1
                            global tax_split1
                                
                            if ai_p_comb_2.get()=="Kerala":
                                tax_choose=ai_comb_p_1_2.get()
                                print(en_str_1.get())
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount1=float(en_str_1.get())*(28/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '18.0% GST(18%)':
                                    tax_amount1=float(en_str_1.get())*(18/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '12.0% GST(12%)':
                                    tax_amount1=float(en_str_1.get())*(12/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '06.0% GST(06%)':
                                    tax_amount1=float(en_str_1.get())*(6/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '05.0% GST(05%)':
                                    tax_amount1=float(en_str_1())*(5/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '03.0% GST(03%)':
                                    tax_amount1=float(en_str_1.get())*(3/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '0.25% GST(0.25%)':
                                    tax_amount1=float(en_str_1.get())*(0.25/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '0.0% GST(0%)' or tax_choose == 'Exempt GST(0%)' or tax_choose == 'Out of Scope(0%)':
                                    tax_amount1=float(en_str_1.get())*(0/100)
                                    tax_split1=tax_amount1/2 

                                elif tax_choose == '28.0% IGST(28%)':
                                    tax_amount1=float(en_str_1.get())*(28/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '18.0% IGST(18%)':
                                    tax_amount1=float(en_str_1.get())*(18/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '12.0% IGST(12%)':
                                    tax_amount1=float(en_str_1.get())*(12/100)
                                    tax_split1=tax_amount1/2 

                                elif tax_choose == '06.0% IGST(06%)':
                                    tax_amount1=float(en_str_1.get())*(6/100)
                                    tax_split1=tax_amount1/2 

                                elif tax_choose == '05.0% IGST(05%)':
                                    tax_amount1=float(en_str_1.get())*(5/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '03.0% IGST(03%)':
                                    tax_amount1=float(en_str_1.get())*(3/100)
                                    tax_split1=tax_amount1/2

                                elif tax_choose == '0.25% IGST(0.25%)':
                                    tax_amount1=float(en_str_1.get())*(0.25/100)
                                    tax_split1=tax_amount1/2
                                
                                elif tax_choose == '0.0% IGST(0%)' or tax_choose == 'Exempt IGST(0%)' :
                                    tax_amount1=float(en_str_1.get())*(0/100)
                                    tax_split1=tax_amount1/2                          
                                else:
                                    pass
                                
                                cgst_entry.delete(0,END)
                                cgst_entry.insert(0,round(tax_split1,2))
                                sgst_entry.delete(0,END)
                                sgst_entry.insert(0,round(tax_split1,2))

                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                            else:
                                tax_choose=ai_comb_p_1_2.get()
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount1=float(en_str_1.get())*(28/100)
                                  
                                elif tax_choose == '18.0% GST(18%)':
                                    tax_amount1=float(en_str_1.get())*(18/100)
                                    

                                elif tax_choose == '12.0% GST(12%)':
                                    tax_amount1=float(en_str_1.get())*(12/100)
                                    

                                elif tax_choose == '06.0% GST(06%)':
                                    tax_amount1=float(en_str_1.get())*(6/100)

                                elif tax_choose == '05.0% GST(05%)':
                                    tax_amount1=float(en_str_1.get())*(5/100)
                                    
                                elif tax_choose == '03.0% GST(03%)':
                                    tax_amount1=float(en_str_1.get())*(3/100)

                                elif tax_choose == '0.25% GST(0.25%)':
                                    tax_amount1=float(en_str_1.get())*(0.25/100)

                                elif tax_choose == '0.0% GST(0%)' or tax_choose == 'Exempt GST(0%)' or tax_choose == 'Out of Scope(0%)':
                                    tax_amount1=float(en_str_1.get())*(0/100)

                                elif tax_choose == '28.0% IGST(28%)':
                                    tax_amount1=float(en_str_1.get())*(28/100)

                                elif tax_choose == '18.0% IGST(18%)':
                                    tax_amount1=float(en_str_1.get())*(18/100)

                                elif tax_choose == '12.0% IGST(12%)':
                                    tax_amount1=float(en_str_1.get())*(12/100)

                                elif tax_choose == '06.0% IGST(06%)':
                                    tax_amount1=float(en_str_1.get())*(6/100)

                                elif tax_choose == '05.0% IGST(05%)':
                                    tax_amount1=float(en_str_1.get())*(5/100)

                                elif tax_choose == '03.0% IGST(03%)':
                                    tax_amount1=float(en_str_1.get())*(3/100)
                                   

                                elif tax_choose == '0.25% IGST(0.25%)':
                                    tax_amount1=float(en_str_1.get())*(0.25/100)
                                  
                                elif tax_choose == '0.0% IGST(0%)' or tax_choose == 'Exempt IGST(0%)' :
                                    tax_amount1=float(en_str_1.get())*(0/100)
                                          
                                else:
                                    pass

                                igst_entry.delete(0,END)
                                igst_entry.insert(0,round(tax_amount1,2))  

                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))    

                        ai_comb_p_1_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_p_1_2['values'] = ['Choose','28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)',
                                    '05.0% GST(05%)','03.0% GST(03%)','0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','28.0% IGST(28%)','18.0% IGST(18%)','12.0% IGST(12%)','06.0% IGST(06%)',
                                    '05.0% IGST(05%)','03.0% IGST(03%)','0.25% IGST(0.25%)','0.0% IGST(0%)','Exempt IGST(0%)','Out of Scope(0%)']
                        ai_comb_p_1_2.current(0)
                        ai_comb_p_1_2.bind("<<ComboboxSelected>>",tax_cal1)
                        window_ai_comb_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_1_2,tags=('aicombo5'))

                        def i_details_2(event):
                            inv_to_str = ai_comb_p_2 .get()
                            sql = "select * from app1_item where name=%s and cid_id=%s"
                            val = (inv_to_str,cmp_dtl[0],)
                            fbcursor.execute(sql,val)
                            inv_c_sel = fbcursor.fetchone()
                            ai_entry_p_2.delete(0,END)
                            ai_entry_p_2.insert(0,inv_c_sel[4])
                            ai_entry_p_2_1.delete('1.0',END)
                            ai_entry_p_2_1.insert('1.0',inv_c_sel[12])
                            ai_entry_2_3.delete(0,END)
                            ai_entry_2_3.insert(0,inv_c_sel[7])
                            p_ava2['text']="Avilable Qty:"+inv_c_sel[18] 

                        sql_pr="select * from auth_user where username=%s"
                        sql_pr_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pr,sql_pr_val,)
                        pr_dtl=fbcursor.fetchone()

                        sql = "select * from app1_company where id_id=%s"
                        val = (pr_dtl[0],)
                        fbcursor.execute(sql, val,)
                        cmp_dtl=fbcursor.fetchone()
                                    

                        sql_pr_cmp="select name from app1_item where cid_id=%s"
                        sql_pr_cmp_val=(cmp_dtl[0],)
                        fbcursor.execute(sql_pr_cmp,sql_pr_cmp_val,)
                        pr_cmp_dtl=fbcursor.fetchall()
                        pi_i1 = []

                        for i in pr_cmp_dtl:
                            pi_i1.append(str(i[0])) 
                        label_2 = Label(inv_canvas_1,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel20'))

                        ai_comb_p_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_p_2 ['values'] = pi_i1
                        window_ai_comb_p_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_2,tags=('aicombo6'))
                        ai_comb_p_2.bind("<<ComboboxSelected>>",i_details_2)

                        taddbtn2=Button(inv_canvas_1,text='+', width=3,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_item)
                        window_tddbtn9 = inv_canvas_1.create_window(0, 0, anchor="nw", window=taddbtn2, tags=('puorderbutton10'))

                        ai_entry_p_2=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_ai_entry_p_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2,tags=('aientry8'))

                        ai_entry_p_2_1=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                        window_ai_entry_p_2_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2_1,tags=('aientry11'))

                        

                        ai_entry_2_3=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_2_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_3,tags=('aientry17'))

                        def multiply_num_i2(event):
                            num1= float(ai_entry_2_2.get())
                            num2= float(ai_entry_2_3.get())
                            mul_i= round(num1 * num2,2)
                            ai_entry_2_4.delete(0, END)
                            ai_entry_2_4.insert(0,mul_i)

                             
                            try:
                                n1 = float(en_str_1.get())
                            except:
                                n1=0.0
                            try:
                                n2 = float(en_str_2.get())
                            except:
                                n2 = 0.0
                            try:
                                n3 = float(en_str_3.get())
                            except:
                                n3 = 0.0
                            try:
                                n4 = float(en_str_4.get())
                            except:
                                n4 = 0.0
                            
                            sum_i = n1+n2+n3+n4
                            sub_entry_1.delete(0, END)
                            sub_entry_1.insert(0,round(sum_i,2))

                            if ai_p_comb_2.get()=="Kerala":
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                            else:
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))

                        ai_entry_2_2=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_2,tags=('aientry14'))
                        ai_entry_2_2.bind("<Button-1>",multiply_num_i2)
        
                        en_str_2 = StringVar()
                        ai_entry_2_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white",textvariable=en_str_2)
                        window_ai_entry_2_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_4,tags=('aientry20'))
                        
                        def tax_cal2(event):
                            tax_choose=ai_comb_P_2_2.get()
                            global tax_amount2
                            tax_amount2=0
                            if ai_p_comb_2.get()=="Kerala":
                                
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount2=float(en_str_2.get())*(28/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                    
                                
                                elif tax_choose =="18.0% GST(18%)":
                                    tax_amount2=float(en_str_2.get())*(18/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                   

                                elif tax_choose =="12.0% GST(12%)":
                                    tax_amount2=float(en_str_2.get())*(12/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                    
                                elif tax_choose =="06.0% GST(06%)":
                                    tax_amount2=float(en_str_2.get())*(6/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                    

                                elif tax_choose =="05.0% GST(05%)":
                                    tax_amount2=float(en_str_2.get())*(5/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                    

                                elif tax_choose =="03.0% GST(03%)":
                                    tax_amount2=float(en_str_2.get())*(3/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                   

                                elif tax_choose =="0.25% GST(0.25%)":
                                    tax_amount2=float(en_str_2.get())*(0.25/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                    

                                elif tax_choose =="0.0% GST(0%)" or tax_choose =="Exempt GST(0%)" or tax_choose =="Out of Scope(0%)":
                                    tax_amount2=float(en_str_2.get())*(0/100)+tax_amount1
                                    tax_split2=tax_amount2/2
                                   
                                elif tax_choose =="28.0% IGST(28%)":
                                    tax_amount2=float(en_str_2.get())*(28/100)+tax_amount1
                                    tax_split2=tax_amount2/2  

                                elif tax_choose =="18.0% IGST(18%)":
                                    tax_amount2=float(en_str_2.get())*(18/100)+tax_amount1
                                    tax_split2=tax_amount2/2 

                                elif tax_choose =="12.0% IGST(12%)":
                                    tax_amount2=float(en_str_2.get())*(12/100)+tax_amount1
                                    tax_split2=tax_amount2/2  

                                elif tax_choose =="06.0% IGST(06%)":
                                    tax_amount2=float(en_str_2.get())*(6/100)+tax_amount1
                                    tax_split2=tax_amount2/2   

                                elif tax_choose =="05.0% IGST(05%)":
                                    tax_amount2=float(en_str_2.get())*(5/100)+tax_amount1
                                    tax_split2=tax_amount2/2   

                                elif tax_choose =="03.0% IGST(03%)":
                                    tax_amount2=float(en_str_2.get())*(3/100)+tax_amount1
                                    tax_split2=tax_amount2/2 

                                elif tax_choose =="0.25% IGST(0.25%)":
                                    tax_amount2=float(en_str_2.get())*(0.25/100)+tax_amount1
                                    tax_split2=tax_amount2/2  

                                elif tax_choose =="0.0% IGST(0%)" or tax_choose =="Exempt IGST(0%)":
                                    tax_amount2=float(en_str_2.get())*(0.25/100)+tax_amount1
                                    tax_split2=tax_amount2/2                                                   
                                       
                                else:
                                    pass
                                cgst_entry.delete(0,END)
                                cgst_entry.insert(0,round(tax_split2,2))
                                sgst_entry.delete(0,END)
                                sgst_entry.insert(0,round(tax_split2,2))
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                                
                           
                            else:
                                
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount2=float(en_str_2.get())*(28/100)+tax_amount1
                                    
                                elif tax_choose =="18.0% GST(18%)":
                                    tax_amount2=float(en_str_2.get())*(18/100)+tax_amount1

                                elif tax_choose =="12.0% GST(12%)":
                                    tax_amount2=float(en_str_2.get())*(12/100)+tax_amount1
                                    
                                elif tax_choose =="06.0% GST(06%)":
                                    tax_amount2=float(en_str_2.get())*(6/100)+tax_amount1
                                    

                                elif tax_choose =="05.0% GST(05%)":
                                    tax_amount2=float(en_str_2.get())*(5/100)+tax_amount1
                                    

                                elif tax_choose =="03.0% GST(03%)":
                                    tax_amount2=float(en_str_2.get())*(3/100)+tax_amount1
                                   

                                elif tax_choose =="0.25% GST(0.25%)":
                                    tax_amount2=float(en_str_2.get())*(0.25/100)+tax_amount1
                                    

                                elif tax_choose =="0.0% GST(0%)" or tax_choose =="Exempt GST(0%)" or tax_choose =="Out of Scope(0%)":
                                    tax_amount2=float(en_str_2.get())*(0/100)+tax_amount1

                                elif tax_choose =="28.0% IGST(28%)":
                                    tax_amount2=float(en_str_2.get())*(28/100)+tax_amount1
                                    

                                elif tax_choose =="18.0% IGST(18%)":
                                    tax_amount2=float(en_str_2.get())*(18/100)+tax_amount1

                                elif tax_choose =="12.0% IGST(12%)":
                                    tax_amount2=float(en_str_2.get())*(12/100)+tax_amount1
                                    

                                elif tax_choose =="06.0% IGST(06%)":
                                    tax_amount2=float(en_str_2.get())*(6/100)+tax_amount1
                                  

                                elif tax_choose =="05.0% IGST(05%)":
                                    tax_amount2=float(en_str_2.get())*(5/100)+tax_amount1
                                      

                                elif tax_choose =="03.0% IGST(03%)":
                                    tax_amount2=float(en_str_2.get())*(3/100)+tax_amount1
                                    

                                elif tax_choose =="0.25% IGST(0.25%)":
                                    tax_amount2=float(en_str_2.get())*(0.25/100)+tax_amount1
                                    

                                elif tax_choose =="0.0% IGST(0%)" or tax_choose =="Exempt IGST(0%)":
                                    tax_amount2=float(en_str_2.get())*(0/100)+tax_amount1                                                 
                                       
                                else:
                                    pass
                                igst_entry.delete(0,END)
                                igst_entry.insert(0,round(tax_amount2,2))

                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                                

                        ai_comb_P_2_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_P_2_2['values'] = ['Choose','28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)',
                                    '05.0% GST(05%)','03.0% GST(03%)','0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','28.0% IGST(28%)','18.0% IGST(18%)','12.0% IGST(12%)','06.0% IGST(06%)',
                                    '05.0% IGST(05%)','03.0% IGST(03%)','0.25% IGST(0.25%)','0.0% IGST(0%)','Exempt IGST(0%)','Out of Scope(0%)']
                        ai_comb_P_2_2.current(0)
                        ai_comb_P_2_2.bind("<<ComboboxSelected>>",tax_cal2) 
                        window_ai_comb_P_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_2_2,tags=('aicombo9'))
                        
                        
                        def i_details_3(event):
                            inv_to_str = ai_comb_p_3 .get()
                            sql = "select * from app1_item where name=%s and cid_id=%s"
                            val = (inv_to_str,cmp_dtl[0],)
                            fbcursor.execute(sql,val)
                            inv_c_sel = fbcursor.fetchone()
                            ai_entry_3.delete(0,END)
                            ai_entry_3.insert(0,inv_c_sel[4])
                            ai_entry_3_1.delete('1.0',END)
                            ai_entry_3_1.insert('1.0',inv_c_sel[12])
                            ai_entry_3_3.delete(0,END)
                            ai_entry_3_3.insert(0,inv_c_sel[7])
                            p_ava3['text']="Avilable Qty:"+inv_c_sel[18] 

                        sql_pr="select * from auth_user where username=%s"
                        sql_pr_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pr,sql_pr_val,)
                        pr_dtl=fbcursor.fetchone()

                        sql = "select * from app1_company where id_id=%s"
                        val = (pr_dtl[0],)
                        fbcursor.execute(sql, val,)
                        cmp_dtl=fbcursor.fetchone()
                                    

                        sql_pr_cmp="select name from app1_item where cid_id=%s"
                        sql_pr_cmp_val=(cmp_dtl[0],)
                        fbcursor.execute(sql_pr_cmp,sql_pr_cmp_val,)
                        pr_cmp_dtl=fbcursor.fetchall()
                        pi_i1 = []

                        for i in pr_cmp_dtl:
                            pi_i1.append(str(i[0])) 

                        label_2 = Label(inv_canvas_1,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel21'))

                        ai_comb_p_3 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_p_3 ['values'] = pi_i1
                        window_ai_comb_p_3 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_3,tags=('aicombo7'))
                        ai_comb_p_3.bind("<<ComboboxSelected>>",i_details_3)

                        taddbtn9=Button(inv_canvas_1,text='+', width=3,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_item)
                        window_tddbtn9 = inv_canvas_1.create_window(0, 0, anchor="nw", window=taddbtn9, tags=('puorderbutton11'))

                        ai_entry_3=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_ai_entry_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3,tags=('aientry9'))

                        ai_entry_3_1=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                        window_ai_entry_3_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_1,tags=('aientry12'))

                        

                        ai_entry_3_3=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_3_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_3,tags=('aientry18'))

                        def multiply_num_i3(event):
                            num1= float(ai_entry_3_2.get())
                            num2= float(ai_entry_3_3.get())
                            mul_i= round(num1 * num2,2)
                            ai_entry_3_4.delete(0, END)
                            ai_entry_3_4.insert(0,mul_i)

                              
                            try:
                                n1 = float(en_str_1.get())
                            except:
                                n1=0.0
                            try:
                                n2 = float(en_str_2.get())
                            except:
                                n2 = 0.0
                            try:
                                n3 = float(en_str_3.get())
                            except:
                                n3 = 0.0
                            try:
                                n4 = float(en_str_4.get())
                            except:
                                n4 = 0.0
                            
                            sum_i = n1+n2+n3+n4
                            sub_entry_1.delete(0, END)
                            sub_entry_1.insert(0,round(sum_i,2))

                            if ai_p_comb_2.get()=="Kerala":
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                            else:
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))


                        en_str_3 = StringVar()
                        ai_entry_3_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white",textvariable=en_str_3)
                        window_ai_entry_3_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_4,tags=('aientry21'))

                        ai_entry_3_2=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_2,tags=('aientry15'))
                        ai_entry_3_2.bind("<Button-1>",multiply_num_i3)


                        def tax_cal3(event):
                            tax_choose=ai_comb_P_3_2.get()
                            global tax_amount3
                            if ai_p_comb_2.get()=="Kerala":
                                
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount3=float(en_str_3.get())*(28/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                    
                                
                                elif tax_choose =="18.0% GST(18%)":
                                    tax_amount3=float(en_str_3.get())*(18/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                   

                                elif tax_choose =="12.0% GST(12%)":
                                    tax_amount3=float(en_str_3.get())*(12/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                    
                                elif tax_choose =="06.0% GST(06%)":
                                    tax_amount3=float(en_str_3.get())*(6/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                    

                                elif tax_choose =="05.0% GST(05%)":
                                    tax_amount3=float(en_str_3.get())*(5/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                    

                                elif tax_choose =="03.0% GST(03%))":
                                    tax_amount3=float(en_str_3.get())*(3/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                   

                                elif tax_choose =="0.25% GST(0.25%)":
                                    tax_amount3=float(en_str_3.get())*(0.25/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                    

                                elif tax_choose =="0.0% GST(0%)" or tax_choose =="Exempt GST(0%)" or tax_choose =="Out of Scope(0%)":
                                    tax_amount3=float(en_str_3.get())*(0/100)+tax_amount2
                                    tax_split3=tax_amount3/2
                                   
                                elif tax_choose =="28.0% IGST(28%)":
                                    tax_amount3=float(en_str_3.get())*(28/100)+tax_amount2
                                    tax_split3=tax_amount3/2  

                                elif tax_choose =="18.0% IGST(18%)":
                                    tax_amount3=float(en_str_3.get())*(18/100)+tax_amount2
                                    tax_split3=tax_amount3/2 

                                elif tax_choose =="12.0% IGST(12%)":
                                    tax_amount3=float(en_str_3.get())*(12/100)+tax_amount2
                                    tax_split3=tax_amount3/2  

                                elif tax_choose =="06.0% IGST(06%)":
                                    tax_amount3=float(en_str_3.get())*(6/100)+tax_amount2
                                    tax_split3=tax_amount3/2   

                                elif tax_choose =="05.0% IGST(05%)":
                                    tax_amount3=float(en_str_3.get())*(5/100)+tax_amount2
                                    tax_split3=tax_amount3/2   

                                elif tax_choose =="03.0% IGST(03%)":
                                    tax_amount3=float(en_str_3.get())*(3/100)+tax_amount2
                                    tax_split3=tax_amount3/2 

                                elif tax_choose =="0.25% IGST(0.25%)":
                                    tax_amount3=float(en_str_3.get())*(0.25/100)+tax_amount2
                                    tax_split3=tax_amount3/2  

                                elif tax_choose =="0.0% IGST(0%)" or tax_choose =="Exempt IGST(0%)":
                                    tax_amount3=float(en_str_3.get())*(0/100)+tax_amount2
                                    tax_split3=tax_amount3/2                                                   
                                       
                                else:
                                    pass
                                cgst_entry.delete(0,END)
                                cgst_entry.insert(0,round(tax_split3,2))
                                sgst_entry.delete(0,END)
                                sgst_entry.insert(0,round(tax_split3,2))

                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                           
                            else:
                                
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount3=float(en_str_3.get())*(28/100)+tax_amount2
                                    
                                elif tax_choose =="18.0% GST(18%)":
                                    tax_amount3=float(en_str_3.get())*(18/100)+tax_amount2

                                elif tax_choose =="12.0% GST(12%)":
                                    tax_amount3=float(en_str_3.get())*(12/100)+tax_amount2
                                    
                                elif tax_choose =="06.0% GST(06%)":
                                    tax_amount3=float(en_str_3.get())*(6/100)+tax_amount2
                                    

                                elif tax_choose =="05.0% GST(05%)":
                                    tax_amount3=float(en_str_3.get())*(5/100)+tax_amount2
                                    

                                elif tax_choose =="03.0% GST(03%))":
                                    tax_amount3=float(en_str_3.get())*(3/100)+tax_amount2
                                   

                                elif tax_choose =="0.25% GST(0.25%)":
                                    tax_amount3=float(en_str_3.get())*(0.25/100)+tax_amount2
                                    

                                elif tax_choose =="0.0% GST(0%)" or tax_choose =="Exempt GST(0%)" or tax_choose =="Out of Scope(0%)":
                                    tax_amount3=float(en_str_3.get())*(0/100)+tax_amount2

                                elif tax_choose =="28.0% IGST(28%)":
                                    tax_amount3=float(en_str_3.get())*(28/100)+tax_amount2
                                    

                                elif tax_choose =="18.0% IGST(18%)":
                                    tax_amount3=float(en_str_3.get())*(18/100)+tax_amount2

                                elif tax_choose =="12.0% IGST(12%)":
                                    tax_amount3=float(en_str_3.get())*(12/100)+tax_amount2
                                    

                                elif tax_choose =="06.0% IGST(06%)":
                                    tax_amount3=float(en_str_3.get())*(6/100)+tax_amount2
                                  

                                elif tax_choose =="05.0% IGST(05%)":
                                    tax_amount3=float(en_str_3.get())*(5/100)+tax_amount2
                                      

                                elif tax_choose =="03.0% IGST(03%)":
                                    tax_amount3=float(en_str_3.get())*(3/100)+tax_amount2
                                    

                                elif tax_choose =="0.25% IGST(0.25%)":
                                    tax_amount3=float(en_str_3.get())*(0.25/100)+tax_amount2
                                    

                                elif tax_choose =="0.0% IGST(0%)" or tax_choose =="Exempt IGST(0%)":
                                    tax_amount3=float(en_str_3.get())*(0/100)+tax_amount2                                                 
                                       
                                else:
                                    pass
                                igst_entry.delete(0,END)
                                igst_entry.insert(0,round(tax_amount3,2))

                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                                
                        

                        ai_comb_P_3_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_P_3_2['values'] = ['Choose','28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)',
                                    '05.0% GST(05%)','03.0% GST(03%)','0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','28.0% IGST(28%)','18.0% IGST(18%)','12.0% IGST(12%)','06.0% IGST(06%)',
                                    '05.0% IGST(05%)','03.0% IGST(03%)','0.25% IGST(0.25%)','0.0% IGST(0%)','Exempt IGST(0%)','Out of Scope(0%)']
                        ai_comb_P_3_2.current(0)
                        ai_comb_P_3_2.bind("<<ComboboxSelected>>",tax_cal3) 
                        window_ai_comb_P_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_3_2,tags=('aicombo10'))
                        
                        def i_details_4(event):
                            inv_to_str = ai_comb_p_4 .get()
                            sql = "select * from app1_item where name=%s and cid_id=%s"
                            val = (inv_to_str,cmp_dtl[0],)
                            fbcursor.execute(sql,val)
                            inv_c_sel = fbcursor.fetchone()
                            ai_entry_4.delete(0,END)
                            ai_entry_4.insert(0,inv_c_sel[4])
                            ai_entry_4_1.delete('1.0',END)
                            ai_entry_4_1.insert('1.0',inv_c_sel[12])
                            ai_entry_4_3.delete(0,END)
                            ai_entry_4_3.insert(0,inv_c_sel[7])
                            p_ava4['text']="Avilable Qty:"+inv_c_sel[18] 

                        sql_pr="select * from auth_user where username=%s"
                        sql_pr_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pr,sql_pr_val,)
                        pr_dtl=fbcursor.fetchone()

                        sql = "select * from app1_company where id_id=%s"
                        val = (pr_dtl[0],)
                        fbcursor.execute(sql, val,)
                        cmp_dtl=fbcursor.fetchone()
                                    

                        sql_pr_cmp="select name from app1_item where cid_id=%s"
                        sql_pr_cmp_val=(cmp_dtl[0],)
                        fbcursor.execute(sql_pr_cmp,sql_pr_cmp_val,)
                        pr_cmp_dtl=fbcursor.fetchall()
                        pi_i1 = []

                        for i in pr_cmp_dtl:
                            pi_i1.append(str(i[0])) 
                        
                        label_2 = Label(inv_canvas_1,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel22'))

                        ai_comb_p_4 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_p_4 ['values'] = pi_i1
                        window_ai_comb_p_4 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_4,tags=('aicombo8'))
                        ai_comb_p_4.bind("<<ComboboxSelected>>",i_details_4)

                        taddbtn9=Button(inv_canvas_1,text='+', width=3,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_item)
                        window_tddbtn9 = inv_canvas_1.create_window(0, 0, anchor="nw", window=taddbtn9, tags=('puorderbutton12'))

                        ai_entry_4=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_ai_entry_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4,tags=('aientry10'))

                        ai_entry_4_1=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                        window_ai_entry_4_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_1,tags=('aientry13'))

                        

                        ai_entry_4_3=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_4_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_3,tags=('aientry19'))

                        def multiply_num_i4(event):
                            num1= float(ai_entry_4_2.get())
                            num2= float(ai_entry_4_3.get())
                            mul_i= round(num1 * num2,2)
                            ai_entry_4_4.delete(0, END)
                            ai_entry_4_4.insert(0,mul_i)

                            
                            try:
                                n1 = float(en_str_1.get())
                            except:
                                n1=0.0
                            try:
                                n2 = float(en_str_2.get())
                            except:
                                n2 = 0.0
                            try:
                                n3 = float(en_str_3.get())
                            except:
                                n3 = 0.0
                            try:
                                n4 = float(en_str_4.get())
                            except:
                                n4 = 0.0
                            
                            sum_i = n1+n2+n3+n4
                            sub_entry_1.delete(0, END)
                            sub_entry_1.insert(0,round(sum_i,2))

                            if ai_p_comb_2.get()=="Kerala":
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                            else:
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
               

                        ai_entry_4_2=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_ai_entry_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_2,tags=('aientry16'))
                        ai_entry_4_2.bind("<Button-1>",multiply_num_i4)
        
                        en_str_4 = StringVar()
                        ai_entry_4_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white",textvariable=en_str_4)
                        window_ai_entry_4_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_4,tags=('aientry22'))
                        
                        def tax_cal4(event):
                            tax_choose=ai_comb_P_4_2.get()
                            global tax_amount4
                            if ai_p_comb_2.get()=="Kerala":
                                
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount4=float(en_str_4.get())*(28/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                    
                                
                                elif tax_choose =="18.0% GST(18%)":
                                    tax_amount4=float(en_str_4.get())*(18/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                   

                                elif tax_choose =="12.0% GST(12%)":
                                    tax_amount4=float(en_str_4.get())*(12/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                    
                                elif tax_choose =="06.0% GST(06%)":
                                    tax_amount4=float(en_str_4.get())*(6/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                    

                                elif tax_choose =="05.0% GST(05%)":
                                    tax_amount4=float(en_str_4.get())*(5/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                    

                                elif tax_choose =="03.0% GST(03%)":
                                    tax_amount4=float(en_str_4.get())*(3/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                   

                                elif tax_choose =="0.25% GST(0.25%)":
                                    tax_amount4=float(en_str_4.get())*(0.25/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                    

                                elif tax_choose =="0.0% GST(0%)" or tax_choose =="Exempt GST(0%)" or tax_choose =="Out of Scope(0%)":
                                    tax_amount4=float(en_str_4.get())*(0/100)+tax_amount3
                                    tax_split4=tax_amount4/2
                                   
                                elif tax_choose =="28.0% IGST(28%)":
                                    tax_amount4=float(en_str_4.get())*(28/100)+tax_amount3
                                    tax_split4=tax_amount4/2  

                                elif tax_choose =="18.0% IGST(18%)":
                                    tax_amount4=float(en_str_4.get())*(18/100)+tax_amount3
                                    tax_split4=tax_amount4/2 

                                elif tax_choose =="12.0% IGST(12%)":
                                    tax_amount4=float(en_str_4.get())*(12/100)+tax_amount3
                                    tax_split4=tax_amount4/2  

                                elif tax_choose =="06.0% IGST(06%)":
                                    tax_amount4=float(en_str_4.get())*(6/100)+tax_amount3
                                    tax_split4=tax_amount4/2   

                                elif tax_choose =="05.0% IGST(05%)":
                                    tax_amount4=float(en_str_4.get())*(5/100)+tax_amount3
                                    tax_split4=tax_amount4/2   

                                elif tax_choose =="03.0% IGST(03%)":
                                    tax_amount4=float(en_str_4.get())*(3/100)+tax_amount3
                                    tax_split4=tax_amount4/2 

                                elif tax_choose =="0.25% IGST(0.25%)":
                                    tax_amount4=float(en_str_4.get())*(0.25/100)+tax_amount3
                                    tax_split4=tax_amount4/2  

                                elif tax_choose =="0.0% IGST(0%)" or tax_choose =="Exempt IGST(0%)":
                                    tax_amount4=float(en_str_4.get())*(0/100)+tax_amount3
                                    tax_split3=tax_amount4/2                                                   
                                       
                                else:
                                    pass
                                sgst_entry.delete(0,END)
                                sgst_entry.insert(0,round(tax_split4,2))
                                cgst_entry.delete(0,END)
                                cgst_entry.insert(0,round(tax_split4,2))

                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                                
                           
                            else:
                                
                                if tax_choose =='Choose':
                                    pass
                                elif tax_choose =="28.0% GST(28%)":
                                    tax_amount4=float(en_str_4.get())*(28/100)+tax_amount3
                                    
                                elif tax_choose =="18.0% GST(18%)":
                                    tax_amount4=float(en_str_4.get())*(18/100)+tax_amount3

                                elif tax_choose =="12.0% GST(12%)":
                                    tax_amount4=float(en_str_4.get())*(12/100)+tax_amount3
                                    
                                elif tax_choose =="06.0% GST(06%)":
                                    tax_amount4=float(en_str_4.get())*(6/100)+tax_amount3
                                    

                                elif tax_choose =="05.0% GST(05%)":
                                    tax_amount4=float(en_str_4.get())*(5/100)+tax_amount3
                                    

                                elif tax_choose =="03.0% GST(03%))":
                                    tax_amount4=float(en_str_4.get())*(3/100)+tax_amount3
                                   

                                elif tax_choose =="0.25% GST(0.25%)":
                                    tax_amount4=float(en_str_4.get())*(0.25/100)+tax_amount3
                                    

                                elif tax_choose =="0.0% GST(0%)" or tax_choose =="Exempt GST(0%)" or tax_choose =="Out of Scope(0%)":
                                    tax_amount4=float(en_str_4.get())*(0/100)+tax_amount3

                                elif tax_choose =="28.0% IGST(28%)":
                                    tax_amount4=float(en_str_4.get())*(28/100)+tax_amount3
                                    

                                elif tax_choose =="18.0% IGST(18%)":
                                    tax_amount4=float(en_str_4.get())*(18/100)+tax_amount3

                                elif tax_choose =="12.0% IGST(12%)":
                                    tax_amount4=float(en_str_4.get())*(12/100)+tax_amount3

                                elif tax_choose =="06.0% IGST(06%)":
                                    tax_amount4=float(en_str_4.get())*(6/100)+tax_amount3
                                  

                                elif tax_choose =="05.0% IGST(05%)":
                                    tax_amount4=float(en_str_4.get())*(5/100)+tax_amount3
                                      

                                elif tax_choose =="03.0% IGST(03%)":
                                    tax_amount4=float(en_str_4.get())*(3/100)+tax_amount3
                                    

                                elif tax_choose =="0.25% IGST(0.25%)":
                                    tax_amount4=float(en_str_4.get())*(0.25/100)+tax_amount3
                                    

                                elif tax_choose =="0.0% IGST(0%)" or tax_choose =="Exempt IGST(0%)":
                                    tax_amount4=float(en_str_4.get())*(0/100)+tax_amount3                                                 
                                       
                                else:
                                    pass
                                igst_entry.delete(0,END)
                                igst_entry.insert(0,round(tax_amount4,2))
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                                

                        ai_comb_P_4_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        ai_comb_P_4_2['values'] = ['Choose','28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)',
                                    '05.0% GST(05%)','03.0% GST(03%)','0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','28.0% IGST(28%)','18.0% IGST(18%)','12.0% IGST(12%)','06.0% IGST(06%)',
                                    '05.0% IGST(05%)','03.0% IGST(03%)','0.25% IGST(0.25%)','0.0% IGST(0%)','Exempt IGST(0%)','Out of Scope(0%)']
                        ai_comb_P_4_2.current(0)
                        ai_comb_P_4_2.bind("<<ComboboxSelected>>",tax_cal4)
                        window_ai_comb_P_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_4_2,tags=('aicombo11'))

                        p_ava1 = Label(inv_canvas_1,height=1, font=('arial 9'),background="#1b3857",fg="white",anchor="w") 
                        window_p_ava1  = inv_canvas_1.create_window(0, 0, anchor="nw", window=p_ava1, tags=("pava1"))
                        
                        p_ava2= Label(inv_canvas_1,height=1, font=('arial 9'),background="#1b3857",fg="white",anchor="w") 
                        window_p_ava2  =inv_canvas_1.create_window(0, 0, anchor="nw", window=p_ava2, tags=("pava2"))

                        p_ava3= Label(inv_canvas_1,height=1, font=('arial 9'),background="#1b3857",fg="white",anchor="w") 
                        window_p_ava3  = inv_canvas_1.create_window(0, 0, anchor="nw", window=p_ava3, tags=("pava3"))

                        p_ava4 = Label(inv_canvas_1,height=1,font=('arial 9'),background="#1b3857",fg="white",anchor="w") 
                        window_p_ava4  = inv_canvas_1.create_window(0, 0, anchor="nw", window=p_ava4, tags=("pava4"))
                        def sto_note(event):
                            if ittsctext4.get('1.0','end-1c')=="Note":
                                ittsctext4.delete(1.0,END)
                            else:
                                pass
                        ittsctext4=scrolledtext.ScrolledText(inv_canvas_1,width=50,background='#2f516f',foreground="white")
                        window_ittsctext4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=100,window=ittsctext4,tags=('notetext'))
                        ittsctext4.insert('1.0','Note')
                        ittsctext4.bind("<Button-1>",sto_note)
                        def invoice_open_file():
                            global filename
                            global p_file
                            filename =askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),("All files", "*.*"),))
                            p_file=os.path.basename(filename)
                            a=shutil.copyfile(filename,os.getcwd()+'/invoicefile/'+p_file)
                            print(a)
                            porder_entry_14.delete(0,END)
                            porder_entry_14.insert(0,p_file)
                        global p_file    
                        p_file=" "
                        porderbtntxt=StringVar()
                        invoicebtn1 = Button(inv_canvas_1,text = 'Choose File',height=1,width=15,foreground="white",background="#1b3857",font='arial 13',command=invoice_open_file)
                        w_invoicebtn1 =inv_canvas_1.create_window(0,0,anchor="nw",window=invoicebtn1 ,tags=("invoicebtn1 "))
                        
                        porder_entry_14=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",font='arial 12')
                        w_porder_entry_14=inv_canvas_1.create_window(0, 0, anchor="nw",height=32, window=porder_entry_14, tags=("invoiceentry"))
                        porder_entry_14.insert(0,'No file choosen')

                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine16'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine17'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine18'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine19'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine20'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine21'))
                        p_line=inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine23'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine24'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine25'))
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine26'))
                        
                        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine27'))
                        

                        label_5 = Label(inv_canvas_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel23'))

                        label_cgst = Label(inv_canvas_1,width=10,height=1,text="CGST", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_cgst = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_cgst,tags=('ailabel29'))

                        label_sgst = Label(inv_canvas_1,width=10,height=1,text="SGST", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_sgst = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_sgst,tags=('ailabel30'))
                        
                        label_igst= Label(inv_canvas_1,width=10,height=1,text="IGST", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_igst = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_igst,tags=('ailabel31'),state=HIDDEN)
                        def cess_cal(event):
                            if tsc_comb.get()=='Select Tax':
                                tsc_entry.delete(0,END)
                            elif tsc_comb.get()== 'Cess 1%' :
                                cess_sum = float(sub_entry_1.get())*0.01
                                cess_round=round(cess_sum,0)
                                tsc_entry.delete(0,END) 
                                tsc_entry.insert(0,cess_round)

                            if ai_p_comb_2.get()=="Kerala":
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(cgst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n3= float(sgst_entry.get())    
                                except:
                                    n3=0.0 
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n3+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))
                            else:
                                try:
                                    n1=float(sub_entry_1.get())
                                except:
                                    n1=0.0
                                try:
                                    n2=float(igst_entry.get())
                                except:
                                    n2=0.0
                                try:
                                    n4= float(tsc_entry.get()) 
                                except:
                                    n4=0.0
                                
                                p_total=n1+n2+n4
                                round_in.delete(0,END)
                                round_in.insert(0,round(p_total,0))
                                grand_entry_1.delete(0,END)
                                grand_entry_1.insert(0,round(p_total,0))    

                         
                        tsc_comb = ttk.Combobox(inv_canvas_1,font=('arial 10'),background='#2f516f')
                        tsc_comb['values'] = ['Select Tax','Cess 1%']
                        tsc_comb.current(0)
                        tsc_comb.bind("<<ComboboxSelected>>",cess_cal)
                        window_tsc_comb  = inv_canvas_1.create_window(0, 0, anchor="nw", width=125,height=32,window=tsc_comb,tags=('tsc_comb'))
                        

                        label_5 = Label(inv_canvas_1,height=1,text="TSC", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel32'))

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Rounf Off", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel24'))

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel25'))

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel26'))

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel27'))

                        
                        sub_str=StringVar()
                        sub_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=sub_str)
                        window_sub_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=sub_entry_1,tags=('aientry23'))

                        cgst=StringVar()
                        cgst_entry=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=cgst)
                        window_cgst_entry= inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=cgst_entry,tags=('aientry29'))

                        sgst=StringVar()
                        sgst_entry=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=sgst)
                        window_sgst_entry= inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=sgst_entry,tags=('aientry30'))

                        igst=StringVar()
                        igst_entry=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=igst)
                        window_igst_entry= inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=igst_entry,tags=('aientry31'),state=HIDDEN)

                        tsc_entry=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_tsc_entry= inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=tsc_entry,tags=('aientry32'))
                        
                        round_in_str=StringVar()
                        round_in=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=round_in_str)
                        window_tax_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=round_in,tags=('aientry24'))

                        grd_str=StringVar()
                        grand_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=grd_str)
                        window_grand_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=grand_entry_1,tags=('aientry25'))

                        
                        amount_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_amount_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=amount_entry_1,tags=('aientry26'))

                        bal_str=StringVar()
                        bal_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT, background='#2f516f',foreground="white",textvariable=bal_str)
                        window_bal_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bal_entry_1,tags=('aientry27'))

                        ai_save_btn1=Button(inv_canvas_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_new_inv)
                        window_ai_save_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=ai_save_btn1,tags=('aibutton2'))

                                              
                   

                        label_5 = Label(inv_canvas_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('bilabl1'),state=HIDDEN)

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('bilabl2'),state=HIDDEN)

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('bilabl3'),state=HIDDEN)

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('bilabl4'),state=HIDDEN)

                        label_5 = Label(inv_canvas_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('bilabl5'),state=HIDDEN)

                        bsub_str=StringVar()
                        bsub_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=bsub_str)
                        bsub_entry_1.insert(0,0)
                        
                        window_bsub_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bsub_entry_1,tags=('bient29'),state=HIDDEN)
                        
                        
                        btax_str=StringVar()
                        btax_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=btax_str)
                        btax_entry_1.insert(0,0)
                        window_btax_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=btax_entry_1,tags=('bient30'),state=HIDDEN)

                        bgrd_str=StringVar()
                        bgrand_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white",textvariable=bgrd_str)
                        bgrand_entry_1.insert(0,0)
                        window_bgrand_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bgrand_entry_1,tags=('bient31'),state=HIDDEN)

                        
                        bamount_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        bamount_entry_1.insert(0,0)
                        window_bamount_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bamount_entry_1,tags=('bient32'),state=HIDDEN)

                        bbal_str=StringVar()
                        bbal_entry_1=Entry(inv_canvas_1,width=30,justify=LEFT, background='#2f516f',foreground="white",textvariable=bbal_str)
                        bbal_entry_1.insert(0,0)
                        window_bbal_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bbal_entry_1,tags=('bient33'),state=HIDDEN)

                        bai_save_btn1=Button(inv_canvas_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_new_inv)
                        window_bai_save_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=bai_save_btn1,tags=('bbutn1'),state=HIDDEN)

                        
                        def inv_back_1_():
                            inv_frame_1.grid_forget()
                            inv_frame.grid(row=0,column=0,sticky='nsew')

                        bck_btn1=Button(inv_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
                        window_bck_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('aibutton3'))

                        label_2 = Label(inv_canvas_1,width=14,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel7'))

                        label_2 = Label(inv_canvas_1,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel28'))



                        def term_date(event):
                            current_date = aid_entry_1.get()
                            current_date_temp = datetime.datetime.strptime(current_date, "%m/%d/%y")
                            if comb_t_2.get() == 'Due on Receipt':
                                newdate = current_date_temp + datetime.timedelta(days=0)
                                aid_entry_2.delete(0, END)
                                aid_entry_2.set_date(newdate)
                            elif comb_t_2.get() == 'NET 15':
                                newdate = current_date_temp + datetime.timedelta(days=15)
                                aid_entry_2.delete(0, END)
                                aid_entry_2.set_date(newdate)
                            elif comb_t_2.get() == 'NET 30':
                                newdate = current_date_temp + datetime.timedelta(days=30)
                                aid_entry_2.delete(0, END)
                                aid_entry_2.set_date(newdate)
                            elif comb_t_2.get() == 'NET 60':
                                newdate = current_date_temp + datetime.timedelta(days=60)
                                aid_entry_2.delete(0, END)
                                aid_entry_2.set_date(newdate)
                            elif comb_t_2.get() == 'Add New Term':
                                pass
                            else:
                                pass

                        comb_t_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                        comb_t_2['values'] = ("Due on Receipt","NET 15","NET 30","NET 60","Add New Term",)
                        window_comb_t_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=comb_t_2,tags=('aicombo2'))
                        comb_t_2.bind("<<ComboboxSelected>>",term_date)

                        aid_entry_1=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
                        window_aid_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_1,tags=('aidate1'))

                        aid_entry_2=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
                        window_aid_entry_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_2,tags=('aidate2'))



 def sales_add_new_inv():

                            customername = aicomb_1.get()
                            email = aientry_1.get()
                            terms = comb_t_2.get()
                            invoicedate = aid_entry_1.get_date()
                            duedate = aid_entry_2.get_date()
                            bname = ai_b_entry_1.get('1.0', 'end-1c')
                            placosupply = ai_p_comb_2.get()

                            product = ai_comb_p_1.get()
                            hsn = ai_entry_p_1.get()
                            description = ai_entry_p_1_2.get('1.0', 'end-1c')
                            qty = ai_entry_p_1_3.get()
                            price = ai_entry_p_1_4.get()
                            total = en_str_1.get()
                            tax = ai_comb_p_1_2.get()
                            product2 = ai_comb_p_2.get()
                            hsn2 = ai_entry_p_2.get()
                            description2 = ai_entry_p_2_1.get('1.0', 'end-1c')
                            qty2 = ai_entry_2_2.get()
                            price2 = ai_entry_2_3.get()
                            total2 = ai_entry_2_4.get()
                            tax2 = ai_comb_P_2_2.get()
                            product3 = ai_comb_p_3.get()
                            hsn3 = ai_entry_3.get()
                            description3 = ai_entry_3_1.get('1.0', 'end-1c')
                            qty3 = ai_entry_3_2.get()
                            price3 = ai_entry_3_3.get()
                            total3 = ai_entry_3_4.get()
                            tax3 = ai_comb_P_3_2.get()
                            product4 = ai_comb_p_4.get()
                            hsn4 = ai_entry_4.get()
                            description4 = ai_entry_4_1.get('1.0', 'end-1c')
                            qty4 = ai_entry_4_2.get()
                            price4 = ai_entry_4_3.get()
                            total4 = ai_entry_4_4.get()
                            tax4 = ai_comb_P_4_2.get()
                            notice = ittsctext4.get(1.0,END)
                            status ="Draft"
                            subtotal = sub_entry_1.get()
                            cgst = cgst_entry.get()
                            sgst = sgst_entry.get()
                            igst = igst_entry.get()
                            tsc = tsc_entry.get()
                            roundoff = round_in.get()
                            grandtotal= grand_entry_1.get()
                            amountrec= amount_entry_1.get()
                            bal= bal_entry_1.get()
                            
                            

                            usr_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usr_val = (nm_ent.get(),)
                            fbcursor.execute(usr_sql,usr_val)
                            usr_data = fbcursor.fetchone()

                            cmp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmp_val = (usr_data[0],)
                            fbcursor.execute(cmp_sql,cmp_val)
                            cmp_data = fbcursor.fetchone()
                            cid = cmp_data[0]

                            ref_sql = "SELECT invoiceid FROM app1_invoice WHERE cid_id=%s"
                            ref_val = (cid,)
                            fbcursor.execute(ref_sql,ref_val)
                            ref_data = fbcursor.fetchone()
                            if terms=="Add New Term":
                                terms="NET "+ein_b_entry_1.get()
                            
                            if ref_data is not None:
                                
                                ref1_sql = "SELECT max(invoiceno) FROM app1_invoice WHERE cid_id=%s"
                                ref1_val = (cid,)
                                fbcursor.execute(ref1_sql,ref1_val)
                                ref1_data = fbcursor.fetchone() 
                                
                                invoiceno=int(ref1_data[0])+1
                            else:
                                invoiceno=1000

                            if customername =="Choose..." or  placosupply=="Choose...":
                                pass
                            else:
                                if p_file==" ":      
                                        file=None
                                else:
                                        file=p_file

                                if notice=="Note":
                                    notice=None 

                                if tax=="Choose":
                                        tax=None
                                if tax2 =="Choose":
                                    tax2=None
                                if tax3=="Choose":
                                    tax3=None
                                if tax4=="Choose":
                                    tax4=None    

                                if qty=="0":
                                    qty=None
                                if qty2 =="0":
                                    qty2=None
                                if qty3=="0":
                                    qty3=None
                                if qty4=="0":
                                    qty4=None       
                                
                                if price=="0":
                                    price=None
                                if price2 =="0":
                                    price2=None
                                if price3=="0":
                                    price3=None
                                if price4=="0":
                                    price4=None  

                                if total=="0":
                                    total=None
                                if total2 =="0":
                                    total2 =None
                                if total3 =="0":
                                    total3 =None
                                if total4 =="0":
                                    total4=None         

                                       
                                inv_sql_1 = "INSERT INTO app1_invoice (customername,email,invoiceno,terms,invoicedate,duedate,bname,placosupply,amtrecvd,baldue,subtotal,grandtotal,status,note,file,IGST,CGST,SGST,TCS,product,hsn,description,qty,price,total,tax,product2,hsn2,description2,qty2,price2,total2,tax2,product3,hsn3,description3,qty3,price3,total3,tax3,product4,hsn4,description4,qty4,price4,total4,tax4,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                inv_val_1=(customername,email,invoiceno,terms,invoicedate,duedate,bname,placosupply,amountrec,bal,subtotal,grandtotal,status,notice,file,igst,cgst,sgst,tsc,product,hsn,description,qty,price,total,tax,product2,hsn2,description2,qty2,price2,total2,tax2,product3,hsn3,description3,qty3,price3,total3,tax3,product4,hsn4,description4,qty4,price4,total4,tax4,cid)
                                fbcursor.execute(inv_sql_1,inv_val_1)
                                finsysdb.commit()
                              
                            #----------Refresh Insert Tree--------#

                            for record in inv_tree.get_children():
                                    inv_tree.delete(record)

                            sql_pr="select * from auth_user where username=%s"
                            sql_pr_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pr,sql_pr_val,)
                            pr_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtl=fbcursor.fetchone()

                            c_sql_1 = "SELECT * FROM app1_invoice where cid_id=%s"
                            c_val_1 = (cmp_dtl[0],)
                            fbcursor.execute(c_sql_1,c_val_1,)
                            i_data_1 = fbcursor.fetchall()

                            count0 = 0
                            for i in i_data_1:
                                if True:
                                    inv_tree.insert(parent='',index='end',iid=i,text='',values=(i[5],i[3],i[13],i[1],i[14],i[6],i[12],i[10])) 
                                else:
                                    pass
                            count0 += 1

                                
                            inv_frame_1.destroy()
                            inv_frame.grid(row=0,column=0,sticky='nsew')