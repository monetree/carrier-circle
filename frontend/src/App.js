import React, { Component } from 'react';
import 'App.css';
import Table from 'components/Table/Table';



class App extends Component {
	constructor(props){
		super(props)
		this.state = {
			data: []
		}
	}

	fetchJob = (url) => {
		fetch('http://127.0.0.1:3000' + url + '?token=thinkonce')
		.then(response => response.json())
		.then(res => {
			if (this.state.data !== []){
				this.setState({ data: res })
				console.log(this.state.data)
			}
		})
		
		
	}

  render() {
    return (
      <div>
		<div className="page" >
				<div className="page-main">
					<div className="header">
						<div className="container">
							<div className="d-flex">
								<a className="header-brand" href="index.html">
									<img src="assets/images/brand/logo.png" className="header-brand-img" alt="adminor logo" />
								</a>
								<div className="d-flex order-lg-2 ml-auto header-right-icons">
									<div className="p-2">
										<form className="input-icon ">
											<div className="input-icon-addon">
												<i className="fe fe-search"></i>
											</div>
											<input type="search" className="form-control header-search" placeholder="Search&hellip;" />
										</form>
									</div>
									<div className="dropdown d-none d-md-flex" >
										<span  className="nav-link icon full-screen-link nav-link-bg">
											<i className="fa fa-expand"  id="fullscreen-button"></i>
										</span>
									</div>
									<div className="dropdown d-none d-md-flex">
										<span className="nav-link icon" data-toggle="dropdown">
											<i className="fa fa-bell-o"></i>
											<span className="nav-unread bg-warning"></span>
										</span>
										<div className="dropdown-menu dropdown-menu-right dropdown-menu-arrow">
											<span className="dropdown-item d-flex pb-3">
												<div className="notifyimg">
													<i className="fa fa-thumbs-o-up"></i>
												</div>
												<div>
													<strong>Someone likes our posts.</strong>
													<div className="small text-muted">3 hours ago</div>
												</div>
											</span>
											<span className="dropdown-item d-flex pb-3">
												<div className="notifyimg">
													<i className="fa fa-commenting-o"></i>
												</div>
												<div>
													<strong> 3 New Comments</strong>
													<div className="small text-muted">5  hour ago</div>
												</div>
											</span>
											<span className="dropdown-item d-flex pb-3">
												<div className="notifyimg">
													<i className="fa fa-cogs"></i>
												</div>
												<div>
													<strong> Server Rebooted.</strong>
													<div className="small text-muted">45 mintues ago</div>
												</div>
											</span>
											<div className="dropdown-divider"></div>
											<span className="dropdown-item text-center">View all Notification</span>
										</div>
									</div>
									<div className="dropdown d-none d-md-flex">
										<span className="nav-link icon text-center" data-toggle="dropdown">
											<i className="icon icon-speech"></i>
											<span className=" nav-unread badge badge-info badge-pill">2</span>
										</span>
										<div className="dropdown-menu dropdown-menu-right dropdown-menu-arrow">
											<span className="dropdown-item text-center">2 New Messages</span>
											<div className="dropdown-divider"></div>
											<span className="dropdown-item d-flex pb-3">
												<span className="avatar brround mr-3 align-self-center cover-image" data-image-src="assets/images/faces/male/41.jpg"></span>
												<div>
													<strong>Madeleine</strong> Hey! there I' am available....
													<div className="small text-muted">3 hours ago</div>
												</div>
											</span>
											<span className="dropdown-item d-flex pb-3">
												<span className="avatar brround mr-3 align-self-center cover-image" data-image-src="assets/images/faces/female/1.jpg"></span>
												<div>
													<strong>Anthony</strong> New product Launching...
													<div className="small text-muted">5  hour ago</div>
												</div>
											</span>
											<span className="dropdown-item d-flex pb-3">
												<span className="avatar brround mr-3 align-self-center cover-image" data-image-src= "assets/images/faces/female/18.jpg"></span>
												<div>
													<strong>Olivia</strong> New Schedule Realease......
													<div className="small text-muted">45 mintues ago</div>
												</div>
											</span>
											<div className="dropdown-divider"></div>
											<span className="dropdown-item text-center">See all Messages</span>
										</div>
									</div>
									<div className="dropdown d-none d-md-flex ">
										<span className="nav-link icon " data-toggle="dropdown">
											<i className="fe fe-grid floating"></i>
										</span>
										<div className="dropdown-menu dropdown-menu-right dropdown-menu-arrow">
											<ul className="drop-icon-wrap p-1">
												<li>
													<a href="email.html" className="drop-icon-item">
														<i className="fe fe-mail text-dark"></i>
														<span className="block"> E-mail</span>
													</a>
												</li>
												<li>
													<a href="calendar2.html" className="drop-icon-item">
														<i className="fe fe-calendar text-dark"></i>
														<span className="block">calendar</span>
													</a>
												</li>
												<li>
													<a href="maps.html" className="drop-icon-item">
														<i className="fe fe-map-pin text-dark"></i>
														<span className="block">map</span>
													</a>
												</li>
												<li>
													<a href="cart.html" className="drop-icon-item">
														<i className="fe fe-shopping-cart text-dark"></i>
														<span className="block">Cart</span>
													</a>
												</li>
												<li>
													<a href="chat.html" className="drop-icon-item">
														<i className="fe fe-message-square text-dark"></i>
														<span className="block">chat</span>
													</a>
												</li>
												<li>
													<a href="profile.html" className="drop-icon-item">
														<i className="fe fe-phone-outgoing text-dark"></i>
														<span className="block">contact</span>
													</a>
												</li>
											</ul>
											<div className="dropdown-divider"></div>
											<span className="dropdown-item text-center">View all</span>
										</div>
									</div>
									<div className="dropdown text-center selector">
										<span className="nav-link leading-none" data-toggle="dropdown">
											<span className="avatar avatar-sm brround cover-image" data-image-src="assets/images/faces/female/25.jpg"></span>
										</span>
										<div className="dropdown-menu dropdown-menu-right dropdown-menu-arrow ">
											<div className="text-center">
												<span className="dropdown-item text-center font-weight-sembold user" data-toggle="dropdown">Joyce Stewart</span>
												<span className="text-center user-semi-title text-dark">web designer</span>
												<div className="dropdown-divider"></div>
											</div>
											<span className="dropdown-item">
												<i className="dropdown-icon mdi mdi-account-outline"></i> Profile
											</span>
											<span className="dropdown-item">
												<i className="dropdown-icon  mdi mdi-settings"></i> Settings
											</span>
											<span className="dropdown-item">
												<span className="float-right"><span className="badge badge-primary">6</span></span>
												<i className="dropdown-icon mdi  mdi-message-outline"></i> Inbox
											</span>
											<span className="dropdown-item">
												<i className="dropdown-icon mdi mdi-comment-check-outline"></i> Message
											</span>
											<div className="dropdown-divider"></div>
											<span className="dropdown-item">
												<i className="dropdown-icon mdi mdi-compass-outline"></i> Need help?
											</span>
											<span className="dropdown-item" href="login.html">
												<i className="dropdown-icon mdi  mdi-logout-variant"></i> Sign out
											</span>
										</div>
									</div>
								</div>
								<span className="header-toggler d-lg-none ml-3 ml-lg-0" data-toggle="collapse" data-target="#headerMenuCollapse">
									<span className="header-toggler-icon"></span>
								</span>
							</div>
						</div>

					</div>
					<div className="admin-navbar" id="headerMenuCollapse">
						<div className="container">
							<ul className="nav">
								<li className="nav-item with-sub">
									<span className="nav-link active">
										<i className="fa fa-caret-down"></i>
										<span> All India Govt Jobs</span>
									</span>
									<div className="sub-item">
										<ul>
											<li>
												<a href="index.html">Upsc</a>
											</li>
											<li>
												<a href="index2.html">Ssc</a>
											</li>
											<li>
												<a onClick={() => this.fetchJob('/api/all_india-govt-jobs/other-all-india-govt-jobs/')}>Other All India Jobs</a>
											</li>
										</ul>
									</div>
								</li>
								<li className="nav-item with-sub mega-dropdown">
									<span className="nav-link" href="#"><i className="fa fa-caret-down"></i> 
										<span>StateWise Govt Jobs</span></span>
									<div className="sub-item">
										<div className="row">
											<div className="col-lg-12">
												<div className="row">
													<div className="col">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/andaman-nicobar-govt-jobs/')}>Andaman-Nicobar</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/andhra-pradesh-govt-jobs/')}>Andhra Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/arunachal-pradesh-govt-jobs/')}>Arunachal Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/assam-govt-jobs/')}>Assam</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/bihar-govt-jobs/')}>Bihar</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/chandigarh-govt-jobs/')}>Chandigarh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/chhattishgarh-govt-jobs/')}>Chhattisgarh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/dadra-nagar-haweli-govt-jobs/')}>Dadra-Nagar Haveli</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/daman-diu-govt-jobs/')}>Daman-Diu</a>
															</li>
														</ul>
													</div>
													<div className="col-lg">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/delhi-govt-jobs/')}>Delhi</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/goa-govt-jobs/')}>Goa</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/gujurat-govt-jobs/')}>Gujarat</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/haryana-govt-jobs/')}>Haryana</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/himachal-pradesh-govt-jobs/')}>Himachal Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/jammu-kashmir-govt-jobs/')}>Jammu-Kashmir</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/jharkhand-govt-jobs/')}>Jharkhand</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/karnataka-govt-jobs/')}>Karnataka</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/kerala-govt-jobs/')}>Kerala</a>
															</li>
														</ul>
													</div>
													<div className="col-lg mg-t-30 mg-lg-t-0">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/lakshadweep-govt-jobs/')}>Lakshadweep</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/madhya-pradesh-govt-jobs/')}>Madhya Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/maharashtra-govt-jobs/')}>Maharashtra</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/manipur-govt-jobs/')}>Manipur</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/meghalaya-govt-jobs/')}>Meghalaya</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/mizoram-govt-jobs/')}>Mizoram</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/nagaland-govt-jobs/')}>Nagaland</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/odisha-govt-jobs/')}>Odisha</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/puduchhery-govt-jobs/')}>Puduchhery</a>
															</li>
														</ul>
													</div>
													<div className="col-lg mg-t-30 mg-lg-t-0">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/punjab-govt-jobs/')}>Punjab</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/rajastan-govt-jobs/')}>Rajasthan</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/sikkim-govt-jobs/')}>Sikkim</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/tamilnadu-govt-jobs/')}>Tamil Nadu</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/telengana-govt-jobs/')}>Telangana</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/tripura-govt-jobs/')}>Tripura</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/uttarakhand-govt-jobs/')}>Uttarakhand</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/uttar-pradesh-govt-jobs/')}>Uttar Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-govt-jobs/west-bengal-govt-jobs/')}>West Bengal</a>
															</li>
														</ul>
													</div>

												</div>
											</div>
										</div>
									</div>
								</li>

								<li className="nav-item with-sub">
									<span className="nav-link"><i className="fa fa-caret-down"></i> <span>Bank Jobs</span></span>
									<div className="sub-item">
										<ul>
											<li>
												<a onClick={() => this.fetchJob('/api/bank-jobs/all-bank-jobs/')}>Bank Jobs</a>
											</li>
											<li>
												<a onClick={() => this.fetchJob('/api/bank-jobs/other-financial-jobs/')}>Financial Jobs</a>
											</li>
										</ul>
									</div>
								</li>
								<li className="nav-item with-sub mega-dropdown">
									<span className="nav-link" href="#"><i className="fa fa-caret-down"></i> 
					<span>Teaching Jobs</span></span>
					<div className="sub-item">
										<div className="row">
											<div className="col-lg-12">
												<div className="row">
													<div className="col">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/andaman-nicobar-teaching-jobs/')}>Andaman-Nicobar</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/andhra-pradesh-teaching-jobs/')}>Andhra Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/arunachal-pradesh-teaching-jobs/')}>Arunachal Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/assam-teaching-jobs/')}>Assam</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/bihar-teaching-jobs/')}>Bihar</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/chandigarh-teaching-jobs/')}>Chandigarh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/chhattishgarh-teaching-jobs/')}>Chhattisgarh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/dadra-nagar-haweli-teaching-jobs/')}>Dadra-Nagar Haveli</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/daman-diu-teaching-jobs/')}>Daman-Diu</a>
															</li>
														</ul>
													</div>
													<div className="col-lg">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/delhi-teaching-jobs/')}>Delhi</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/goa-teaching-jobs/')}>Goa</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/gujurat-teaching-jobs/')}>Gujarat</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/haryana-teaching-jobs/')}>Haryana</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/himachal-pradesh-teaching-jobs/')}>Himachal Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/jammu-kashmir-teaching-jobs/')}>Jammu-Kashmir</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/jharkhand-teaching-jobs/')}>Jharkhand</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/karnataka-teaching-jobs/')}>Karnataka</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/kerala-teaching-jobs/')}>Kerala</a>
															</li>
														</ul>
													</div>
													<div className="col-lg mg-t-30 mg-lg-t-0">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/lakshadweep-teaching-jobs/')}>Lakshadweep</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/madhya-pradesh-teaching-jobs/')}>Madhya Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/maharashtra-teaching-jobs/')}>Maharashtra</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/manipur-teaching-jobs/')}>Manipur</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/meghalaya-teaching-jobs/')}>Meghalaya</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/mizoram-teaching-jobs/')}>Mizoram</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/nagaland-teaching-jobs/')}>Nagaland</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/odisha-teaching-jobs/')}>Odisha</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/puduchhery-teaching-jobs/')}>Puduchhery</a>
															</li>
														</ul>
													</div>
													<div className="col-lg mg-t-30 mg-lg-t-0">
														<ul>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/punjab-teaching-jobs/')}>Punjab</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/rajastan-teaching-jobs/')}>Rajasthan</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/sikkim-teaching-jobs/')}>Sikkim</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/tamilnadu-teaching-jobs/')}>Tamil Nadu</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/telengana-teaching-jobs/')}>Telangana</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/tripura-teaching-jobs/')}>Tripura</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/uttarakhand-teaching-jobs/')}>Uttarakhand</a>
															</li>
															<li>
																<a honClick={() => this.fetchJob('/api/statewise-teaching-jobs/uttar-pradesh-teaching-jobs/')}>Uttar Pradesh</a>
															</li>
															<li>
																<a onClick={() => this.fetchJob('/api/statewise-teaching-jobs/west-bengal-teaching-jobs/')}>West Bengal</a>
															</li>
														</ul>
													</div>

												</div>
											</div>
										</div>
									</div>
								</li>
								<li className="nav-item with-sub mega-dropdown">
									<span className="nav-link" href="#">
									<span>Engineering Jobs</span></span>
									
								</li>
								<li className="nav-item with-sub">
									<span className="nav-link" data-toggle="dropdown"> <span onClick={() => this.fetchJob('/api/railway-jobs/')}>Railway Jobs</span></span>
								</li>
								<li className="nav-item with-sub ">
									<span className="nav-link" data-toggle="dropdown"><i className="fa fa-caret-down"></i> 
									<span>Police Defence Jobs</span></span>
									<div className="sub-item">
										<ul>
											<li>
												<a onClick={() => this.fetchJob('/api/police-jobs/all-india-police-defence-jobs/')}>All India</a>
											</li>
											<li>
												<a onClick={() => this.fetchJob('/api/police-jobs/statewise-police-defence-jobs/')}>State Police Jobs</a>
											</li>
										</ul>
									</div>
								</li>
							</ul>
						</div>
					</div>
					<div>
						<div className="container">
							<div className="page-header">
								<h4 className="page-title">Data Tables</h4>
								<ol className="breadcrumb">
									<li className="breadcrumb-item"><span>Pages</span></li>
									<li className="breadcrumb-item active" aria-current="page">Data Tables</li>
								</ol>
							</div>
							<div className="row">
								<div className="col-md-12 col-lg-12">
								{/* find table */}
									<Table data={this.state.data} />
								</div>
							</div>
						</div>
					</div>
				</div>

				<footer className="footer">
					<div className="container">
						<div className="row align-items-center flex-row-reverse">
							<div className="col-lg-12 col-sm-12 mt-3 mt-lg-0 text-center">
								Copyright © 2019 <span>adminor</span>. Designed by <span>Spruko</span> All rights reserved.
							</div>
						</div>
					</div>
				</footer>
			</div>
		</div>

    );
  }
}

export default App;
