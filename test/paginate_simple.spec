require './helper'

describe PaginateSimple do
  before do
    PaginateSimple.config :total => 100 , :page => 1, :per_page => 10
  end
  
  it "should be configured properly" do
    PaginateSimple.total.should eql(100)
    PaginateSimple.current_page.should eql(1)
    PaginateSimple.per_page.should eql(10)
  end

  it "should provide the correct number of pages" do
    PaginateSimple.num_of_pages.should eql(10)
  end
  
  it "should answer to has_next_page? correctly" do
    PaginateSimple.should have_next_page
    PaginateSimple.current_page = 10
    PaginateSimple.should_not have_next_page
  end
  
  it "should answer to has_previous_page? correctly" do
    PaginateSimple.should_not have_previous_page
    PaginateSimple.current_page = 2
    PaginateSimple.should have_next_page
  end
  
  it "should return pages as iterator" do
    PaginateSimple.pages.should respond_to(:each)
    PaginateSimple.current_page = 1
    PaginateSimple.total = 0
    PaginateSimple.pages.should respond_to(:each)
  end
  
  it "should return correct num of pages" do
    PaginateSimple.per_page = 3
    PaginateSimple.total = 10
    PaginateSimple.should have(4).pages
    
    PaginateSimple.current_page = 1
    PaginateSimple.total = 0
    PaginateSimple.should have(0).pages
  end
  
  it "should provide offset" do
    PaginateSimple.current_page = 2
    PaginateSimple.offset.should eql(10)
  end
  
  it "should return next page or nil otherwise" do
    PaginateSimple.current_page = 4
    PaginateSimple.should have_next_page
    PaginateSimple.next_page.should  eql(5)
    
    PaginateSimple.current_page = 10
    PaginateSimple.should_not have_next_page
    PaginateSimple.next_page.should be_nil
  end
  
  it "should return previous page or nil otherwise" do
    PaginateSimple.current_page = 2
    PaginateSimple.should have_previous_page
    PaginateSimple.previous_page.should eql(1)
    
    PaginateSimple.current_page = 1
    PaginateSimple.should_not have_previous_page
    PaginateSimple.previous_page.should be_nil
  end
  
  it "should raise ArgumentError on negative current_page" do
    lambda { PaginateSimple.current_page = -1 }.should raise_error(ArgumentError)
  end
  
  it "should raise ArgumentError on negative total" do
    lambda { PaginateSimple.total = -1 }.should raise_error(ArgumentError)
  end

end
