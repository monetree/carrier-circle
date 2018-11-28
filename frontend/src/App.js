import React, { Component } from 'react';
import 'App.css';
import Table from 'components/Table/Table';


class App extends Component {
  render() {
    return (
      <div>
    <div class="page" >
			<div class="page-main">
				<div class="header">
					<div class="container">
						<div class="d-flex">
							<a class="header-brand" href="index.html">
								<img src="assets/images/brand/logo.png" class="header-brand-img" alt="adminor logo" />
							</a>
							<div class="d-flex order-lg-2 ml-auto header-right-icons">
								<div class="p-2">
									<form class="input-icon ">
										<div class="input-icon-addon">
											<i class="fe fe-search"></i>
										</div>
										<input type="search" class="form-control header-search" placeholder="Search&hellip;" tabindex="1" />
									</form>
								</div>
								<div class="dropdown d-none d-md-flex" >
									<span  class="nav-link icon full-screen-link nav-link-bg">
										<i class="fa fa-expand"  id="fullscreen-button"></i>
									</span>
								</div>
								<div class="dropdown d-none d-md-flex">
									<span class="nav-link icon" data-toggle="dropdown">
										<i class="fa fa-bell-o"></i>
										<span class="nav-unread bg-warning"></span>
									</span>
									<div class="dropdown-menu dropdown-menu-right dropdown-menu-arrow">
										<span class="dropdown-item d-flex pb-3">
											<div class="notifyimg">
												<i class="fa fa-thumbs-o-up"></i>
											</div>
											<div>
												<strong>Someone likes our posts.</strong>
												<div class="small text-muted">3 hours ago</div>
											</div>
										</span>
										<span class="dropdown-item d-flex pb-3">
											<div class="notifyimg">
												<i class="fa fa-commenting-o"></i>
											</div>
											<div>
												<strong> 3 New Comments</strong>
												<div class="small text-muted">5  hour ago</div>
											</div>
										</span>
										<span class="dropdown-item d-flex pb-3">
											<div class="notifyimg">
												<i class="fa fa-cogs"></i>
											</div>
											<div>
												<strong> Server Rebooted.</strong>
												<div class="small text-muted">45 mintues ago</div>
											</div>
										</span>
										<div class="dropdown-divider"></div>
										<span class="dropdown-item text-center">View all Notification</span>
									</div>
								</div>
								<div class="dropdown d-none d-md-flex">
									<span class="nav-link icon text-center" data-toggle="dropdown">
										<i class="icon icon-speech"></i>
										<span class=" nav-unread badge badge-info badge-pill">2</span>
									</span>
									<div class="dropdown-menu dropdown-menu-right dropdown-menu-arrow">
										<span class="dropdown-item text-center">2 New Messages</span>
										<div class="dropdown-divider"></div>
										<span class="dropdown-item d-flex pb-3">
											<span class="avatar brround mr-3 align-self-center cover-image" data-image-src="assets/images/faces/male/41.jpg"></span>
											<div>
												<strong>Madeleine</strong> Hey! there I' am available....
												<div class="small text-muted">3 hours ago</div>
											</div>
										</span>
										<span class="dropdown-item d-flex pb-3">
											<span class="avatar brround mr-3 align-self-center cover-image" data-image-src="assets/images/faces/female/1.jpg"></span>
											<div>
												<strong>Anthony</strong> New product Launching...
												<div class="small text-muted">5  hour ago</div>
											</div>
										</span>
										<span class="dropdown-item d-flex pb-3">
											<span class="avatar brround mr-3 align-self-center cover-image" data-image-src= "assets/images/faces/female/18.jpg"></span>
											<div>
												<strong>Olivia</strong> New Schedule Realease......
												<div class="small text-muted">45 mintues ago</div>
											</div>
										</span>
										<div class="dropdown-divider"></div>
										<span class="dropdown-item text-center">See all Messages</span>
									</div>
								</div>
								<div class="dropdown d-none d-md-flex ">
									<span class="nav-link icon " data-toggle="dropdown">
										<i class="fe fe-grid floating"></i>
									</span>
									<div class="dropdown-menu dropdown-menu-right dropdown-menu-arrow">
										<ul class="drop-icon-wrap p-1">
											<li>
												<a href="email.html" class="drop-icon-item">
													<i class="fe fe-mail text-dark"></i>
													<span class="block"> E-mail</span>
												</a>
											</li>
											<li>
												<a href="calendar2.html" class="drop-icon-item">
													<i class="fe fe-calendar text-dark"></i>
													<span class="block">calendar</span>
												</a>
											</li>
											<li>
												<a href="maps.html" class="drop-icon-item">
													<i class="fe fe-map-pin text-dark"></i>
													<span class="block">map</span>
												</a>
											</li>
											<li>
												<a href="cart.html" class="drop-icon-item">
													<i class="fe fe-shopping-cart text-dark"></i>
													<span class="block">Cart</span>
												</a>
											</li>
											<li>
												<a href="chat.html" class="drop-icon-item">
													<i class="fe fe-message-square text-dark"></i>
													<span class="block">chat</span>
												</a>
											</li>
											<li>
												<a href="profile.html" class="drop-icon-item">
													<i class="fe fe-phone-outgoing text-dark"></i>
													<span class="block">contact</span>
												</a>
											</li>
										</ul>
										<div class="dropdown-divider"></div>
										<span class="dropdown-item text-center">View all</span>
									</div>
								</div>
								<div class="dropdown text-center selector">
									<span class="nav-link leading-none" data-toggle="dropdown">
										<span class="avatar avatar-sm brround cover-image" data-image-src="assets/images/faces/female/25.jpg"></span>
									</span>
									<div class="dropdown-menu dropdown-menu-right dropdown-menu-arrow ">
										<div class="text-center">
											<span class="dropdown-item text-center font-weight-sembold user" data-toggle="dropdown">Joyce Stewart</span>
											<span class="text-center user-semi-title text-dark">web designer</span>
											<div class="dropdown-divider"></div>
										</div>
										<span class="dropdown-item">
											<i class="dropdown-icon mdi mdi-account-outline"></i> Profile
										</span>
										<span class="dropdown-item">
											<i class="dropdown-icon  mdi mdi-settings"></i> Settings
										</span>
										<span class="dropdown-item">
											<span class="float-right"><span class="badge badge-primary">6</span></span>
											<i class="dropdown-icon mdi  mdi-message-outline"></i> Inbox
										</span>
										<span class="dropdown-item">
											<i class="dropdown-icon mdi mdi-comment-check-outline"></i> Message
										</span>
										<div class="dropdown-divider"></div>
										<span class="dropdown-item">
											<i class="dropdown-icon mdi mdi-compass-outline"></i> Need help?
										</span>
										<span class="dropdown-item" href="login.html">
											<i class="dropdown-icon mdi  mdi-logout-variant"></i> Sign out
										</span>
									</div>
								</div>
							</div>
							<span class="header-toggler d-lg-none ml-3 ml-lg-0" data-toggle="collapse" data-target="#headerMenuCollapse">
								<span class="header-toggler-icon"></span>
							</span>
						</div>
					</div>

				</div>
				<div class="admin-navbar" id="headerMenuCollapse">
					<div class="container">
						<ul class="nav">
							<li class="nav-item with-sub">
								<span class="nav-link active">
									<i class="fa fa-caret-down"></i>
									<span> All India Govt Jobs</span>
								</span>
								<div class="sub-item">
									<ul>
										<li>
											<a href="index.html">Upsc</a>
										</li>
										<li>
											<a href="index2.html">Ssc</a>
										</li>
										<li>
											<a href="index3.html">Other All India Jobs</a>
										</li>
									</ul>
								</div>
							</li>
							<li class="nav-item with-sub mega-dropdown">
								<span class="nav-link" href="#"><i class="fa fa-caret-down"></i> 
               						 <span>StateWise Govt Jobs</span></span>
								<div class="sub-item">
									<div class="row">
										<div class="col-lg-12">
											<div class="row">
												<div class="col">
													<ul>
														<li>
															<a href="alerts.html">Andaman-Nicobar</a>
														</li>
														<li>
															<a href="buttons.html">Andhra Pradesh</a>
														</li>
														<li>
															<a href="colors.html">Arunachal Pradesh</a>
														</li>
														<li>
															<a href="avatarsquare.html">Assam</a>
														</li>
														<li>
															<a href="avatar-round.html">Bihar</a>
														</li>
														<li>
															<a href="avatar-radius.html">Chandigarh</a>
														</li>
														<li>
															<a href="dropdown.html">Chhattisgarh</a>
														</li>
														<li>
															<a href="dropdown.html">Dadra-Nagar Haveli</a>
														</li>
														<li>
															<a href="dropdown.html">Daman-Diu</a>
														</li>
													</ul>
												</div>
												<div class="col-lg">
													<ul>
														<li>
															<a href="alerts.html">Delhi</a>
														</li>
														<li>
															<a href="buttons.html">Goa</a>
														</li>
														<li>
															<a href="colors.html">Gujarat</a>
														</li>
														<li>
															<a href="avatarsquare.html">Haryana</a>
														</li>
														<li>
															<a href="avatar-round.html">Himachal Pradesh</a>
														</li>
														<li>
															<a href="avatar-radius.html">Jammu-Kashmir</a>
														</li>
														<li>
															<a href="dropdown.html">Jharkhand</a>
														</li>
														<li>
															<a href="dropdown.html">Karnataka</a>
														</li>
														<li>
															<a href="dropdown.html">Kerala</a>
														</li>
													</ul>
												</div>
												<div class="col-lg mg-t-30 mg-lg-t-0">
													<ul>
														<li>
															<a href="alerts.html">Lakshadweep</a>
														</li>
														<li>
															<a href="buttons.html">Madhya Pradesh</a>
														</li>
														<li>
															<a href="colors.html">Maharashtra</a>
														</li>
														<li>
															<a href="avatarsquare.html">Manipur</a>
														</li>
														<li>
															<a href="avatar-round.html">Meghalaya</a>
														</li>
														<li>
															<a href="avatar-radius.html">Mizoram</a>
														</li>
														<li>
															<a href="dropdown.html">Nagaland</a>
														</li>
														<li>
															<a href="dropdown.html">Odisha</a>
														</li>
														<li>
															<a href="dropdown.html">Puduchhery</a>
														</li>
													</ul>
												</div>
												<div class="col-lg mg-t-30 mg-lg-t-0">
													<ul>
														<li>
															<a href="alerts.html">Punjab</a>
														</li>
														<li>
															<a href="buttons.html">Rajasthan</a>
														</li>
														<li>
															<a href="colors.html">Sikkim</a>
														</li>
														<li>
															<a href="avatarsquare.html">Tamil Nadu</a>
														</li>
														<li>
															<a href="avatar-round.html">Telangana</a>
														</li>
														<li>
															<a href="avatar-radius.html">Tripura</a>
														</li>
														<li>
															<a href="dropdown.html">Uttarakhand</a>
														</li>
														<li>
															<a href="dropdown.html">Uttar Pradesh</a>
														</li>
														<li>
															<a href="dropdown.html">West Bengal</a>
														</li>
													</ul>
												</div>

											</div>
										</div>
									</div>
								</div>
							</li>

							<li class="nav-item with-sub">
								<span class="nav-link"><i class="fa fa-caret-down"></i> <span>Bank Jobs</span></span>
								<div class="sub-item">
									<ul>
										<li>
											<a href="widgets.html">Bank Jobs</a>
										</li>
										<li>
											<a href="cards.html">Financial Jobs</a>
										</li>
									</ul>
								</div>
							</li>
							<li class="nav-item with-sub mega-dropdown">
								<span class="nav-link" href="#"><i class="fa fa-caret-down"></i> 
                <span>Teaching Jobs</span></span>
				<div class="sub-item">
									<div class="row">
										<div class="col-lg-12">
											<div class="row">
												<div class="col">
													<ul>
														<li>
															<a href="alerts.html">Andaman-Nicobar</a>
														</li>
														<li>
															<a href="buttons.html">Andhra Pradesh</a>
														</li>
														<li>
															<a href="colors.html">Arunachal Pradesh</a>
														</li>
														<li>
															<a href="avatarsquare.html">Assam</a>
														</li>
														<li>
															<a href="avatar-round.html">Bihar</a>
														</li>
														<li>
															<a href="avatar-radius.html">Chandigarh</a>
														</li>
														<li>
															<a href="dropdown.html">Chhattisgarh</a>
														</li>
														<li>
															<a href="dropdown.html">Dadra-Nagar Haveli</a>
														</li>
														<li>
															<a href="dropdown.html">Daman-Diu</a>
														</li>
													</ul>
												</div>
												<div class="col-lg">
													<ul>
														<li>
															<a href="alerts.html">Delhi</a>
														</li>
														<li>
															<a href="buttons.html">Goa</a>
														</li>
														<li>
															<a href="colors.html">Gujarat</a>
														</li>
														<li>
															<a href="avatarsquare.html">Haryana</a>
														</li>
														<li>
															<a href="avatar-round.html">Himachal Pradesh</a>
														</li>
														<li>
															<a href="avatar-radius.html">Jammu-Kashmir</a>
														</li>
														<li>
															<a href="dropdown.html">Jharkhand</a>
														</li>
														<li>
															<a href="dropdown.html">Karnataka</a>
														</li>
														<li>
															<a href="dropdown.html">Kerala</a>
														</li>
													</ul>
												</div>
												<div class="col-lg mg-t-30 mg-lg-t-0">
													<ul>
														<li>
															<a href="alerts.html">Lakshadweep</a>
														</li>
														<li>
															<a href="buttons.html">Madhya Pradesh</a>
														</li>
														<li>
															<a href="colors.html">Maharashtra</a>
														</li>
														<li>
															<a href="avatarsquare.html">Manipur</a>
														</li>
														<li>
															<a href="avatar-round.html">Meghalaya</a>
														</li>
														<li>
															<a href="avatar-radius.html">Mizoram</a>
														</li>
														<li>
															<a href="dropdown.html">Nagaland</a>
														</li>
														<li>
															<a href="dropdown.html">Odisha</a>
														</li>
														<li>
															<a href="dropdown.html">Puduchhery</a>
														</li>
													</ul>
												</div>
												<div class="col-lg mg-t-30 mg-lg-t-0">
													<ul>
														<li>
															<a href="alerts.html">Punjab</a>
														</li>
														<li>
															<a href="buttons.html">Rajasthan</a>
														</li>
														<li>
															<a href="colors.html">Sikkim</a>
														</li>
														<li>
															<a href="avatarsquare.html">Tamil Nadu</a>
														</li>
														<li>
															<a href="avatar-round.html">Telangana</a>
														</li>
														<li>
															<a href="avatar-radius.html">Tripura</a>
														</li>
														<li>
															<a href="dropdown.html">Uttarakhand</a>
														</li>
														<li>
															<a href="dropdown.html">Uttar Pradesh</a>
														</li>
														<li>
															<a href="dropdown.html">West Bengal</a>
														</li>
													</ul>
												</div>

											</div>
										</div>
									</div>
								</div>
							</li>
							<li class="nav-item with-sub mega-dropdown">
								<span class="nav-link" href="#">
               					 <span>Engineering Jobs</span></span>
								<div class="sub-item">
									<div class="row">
										<div class="col-lg-12">
											<label class="section-label">Basic Elements</label>
											<div class="row">
												<div class="col">
													<ul>
														<li>
															<a href="alerts.html">Alerts</a>
														</li>
														<li>
															<a href="buttons.html">Buttons</a>
														</li>
														<li>
															<a href="colors.html">Colors</a>
														</li>
														<li>
															<a href="avatarsquare.html">Avatar-Square</a>
														</li>
														<li>
															<a href="avatar-round.html">Avatar-Rounded</a>
														</li>
														<li>
															<a href="avatar-radius.html">Avatar-Radius</a>
														</li>
														<li>
															<a href="dropdown.html">Drop downs</a>
														</li>
													</ul>
												</div>
												<div class="col-lg">
													<ul>
														<li>
															<a href="list.html">List</a>
														</li>
														<li>
															<a href="tags.html">Tags</a>
														</li>
														<li>
															<a href="pagination.html">Pagination</a>
														</li>
														<li>
															<a href="navigation.html">Navigation</a>
														</li>
														<li>
															<a href="typography.html">Typography</a>
														</li>
														<li>
															<a href="breadcrumbs.html">Breadcrumbs</a>
														</li>
														<li>
															<a href="badge.html">Badges</a>
														</li>
													</ul>
												</div>
												<div class="col-lg mg-t-30 mg-lg-t-0">
													<ul>
														<li>
															<a href="jumbotron.html">Jumbotron</a>
														</li>
														<li>
															<a href="panels.html">Panels</a>
														</li>
														<li>
															<a href="thumbnails.html">Thumbnails</a>
														</li>
														<li>
															<a href="mediaobject.html">Media Object</a>
														</li>
														<li>
															<a href="accordion.html">Accordions</a>
														</li>
														<li>
															<a href="tabs.html">Tabs</a>
														</li>
														<li>
															<a href="chart.html">Charts</a>
														</li>
													</ul>
												</div>
												<div class="col-lg mg-t-30 mg-lg-t-0">
													<ul>
														<li>
															<a href="modal.html">Modal</a>
														</li>
														<li>
															<a href="tooltipandpopover.html">Tooltip and popover</a>
														</li>
														<li>
															<a href="progress.html">Progress</a>
														</li>
														<li>
															<a href="carousel.html">Carousels</a>
														</li>
														<li>
															<a href="headers.html">Headers  </a>
														</li>
														<li>
															<a href="footers.html">Footers  </a>
														</li>
														<li>
															<a href="loaders.html">Loaders</a>
														</li>
													</ul>
												</div>

											</div>
										</div>
									</div>
								</div>
							</li>
							<li class="nav-item with-sub">
								<span class="nav-link" data-toggle="dropdown"> <span>Railway Jobs</span></span>
							

							</li>
							<li class="nav-item with-sub ">
								<span class="nav-link" data-toggle="dropdown"><i class="fa fa-caret-down"></i> 
								<span>Police Defence Jobs</span></span>
								<div class="sub-item">
									<ul>
										<li>
											<a href="maps.html">All India</a>
										</li>
										<li>
											<a href="crypto-currencies.html">State Police Jobs</a>
										</li>
									</ul>
								</div>
							</li>
						</ul>
					</div>
				</div>
				<div>
					<div class="container">
						<div class="page-header">
							<h4 class="page-title">Data Tables</h4>
							<ol class="breadcrumb">
								<li class="breadcrumb-item"><span>Pages</span></li>
								<li class="breadcrumb-item active" aria-current="page">Data Tables</li>
							</ol>
						</div>
						<div class="row">
							<div class="col-md-12 col-lg-12">
							{/* find table */}
								<Table />
							</div>
						</div>
					</div>
				</div>
			</div>

			<footer class="footer">
				<div class="container">
					<div class="row align-items-center flex-row-reverse">
						<div class="col-lg-12 col-sm-12 mt-3 mt-lg-0 text-center">
							Copyright © 2018 <span>adminor</span>. Designed by <span>Spruko</span> All rights reserved.
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
